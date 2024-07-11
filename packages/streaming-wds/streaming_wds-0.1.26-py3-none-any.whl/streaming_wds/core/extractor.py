import logging
import os
import tarfile
import threading
import time
from io import BufferedReader
from queue import Empty, Queue
from typing import Dict, Generator, List, Literal, Union

import pyarrow as pa

from .cache import LocalShardLRUCache

logger = logging.getLogger(__name__)


class ShardExtractor:
    """
    A class for extracting shards and processing their contents.

    This class handles the extraction of shards from a local cache, processes their
    contents, and puts the extracted samples into an output queue.

    Attributes:
        input_queue (Queue): Queue for incoming shard extraction requests.
        output_queue (Queue): Queue for outputting extracted samples.
        stop_event (threading.Event): Event to signal stopping of the extraction process.
        buffer_size (int): Maximum buffer size for memory management.
        cache (LocalShardLRUCache): Local cache for storing and retrieving shards.
        input_finish_event (threading.Event): Event to signal completion of input.
        output_finish_event (threading.Event): Event to signal completion of output.
    """

    def __init__(
        self,
        *,
        input_queue: Queue,
        output_queue: Queue,
        stop_event: threading.Event,
        input_finish_event: threading.Event,
        output_finish_event: threading.Event,
        cache: LocalShardLRUCache,
        memory_buffer_limit_bytes: int,
        mode: Literal["r:*", "r|*"] = "r|*",
    ):
        """
        Initialize the ShardExtractor.

        Args:
            input_queue (Queue): Queue for incoming shard extraction requests.
            output_queue (Queue): Queue for outputting extracted samples.
            stop_event (threading.Event): Event to signal stopping of the extraction process.
            input_finish_event (threading.Event): Event to signal completion of input.
            output_finish_event (threading.Event): Event to signal completion of output.
            cache (LocalShardLRUCache): Local cache for storing and retrieving shards.
            buffer_size (int, optional): Maximum buffer size for memory management. Defaults to 1GB.
            mode (Literal["r:*", "r|*"], optional): Mode for reading tar files. Defaults to "r|*".
        """
        self.cache = cache

        if mode not in ["r:*", "r|*"]:
            raise ValueError("Invalid mode. Must be 'r:*' or 'r|*'")
        self.mode = mode

        self.input_queue = input_queue
        self.output_queue = output_queue
        self.stop_event = stop_event

        self.input_finish_event = input_finish_event
        self.output_finish_event = output_finish_event

        self.memory_buffer_limit_bytes = memory_buffer_limit_bytes
        self.worker_threads = []

    def set_queues(self, *, input_queue: Queue, output_queue: Queue):
        """
        Set the input and output queues for the extractor.

        Args:
            input_queue (Queue): Queue for incoming shard extraction requests.
            output_queue (Queue): Queue for outputting extracted samples.
        """
        self.input_queue = input_queue
        self.output_queue = output_queue

    def tar_member_iterator(self, tar: tarfile.TarFile) -> List[tarfile.TarInfo]:
        """
        Iterate over the members in a tar file based on the specified mode.

        Args:
            tar (tarfile.TarFile): The tar file object to iterate over.

        Yields:
            tarfile.TarInfo: The next member in the tar file.

        Raises:
            ValueError: If the mode is not 'r:*' or 'r|*'.
        """
        if self.mode == "r:*":
            yield from sorted(tar.getmembers(), key=lambda x: x.name)
        elif self.mode == "r|*":
            yield from tar
        else:
            raise ValueError("Invalid mode. Must be 'r:*' or 'r|*'")

    def tar_sample_iterator(
        self, fileobj: BufferedReader, shard_idx: int, rank: int
    ) -> Generator[Dict[str, Union[pa.Buffer, int]], None, None]:
        """
        Iterate over the members in a tar file and yield aggregated data for each sample.

        This method reads the contents of a tar file, processes its files, and yields
        the aggregated data for each sample in the tar file. The aggregation is based
        on the sample key derived from the file names.

        Args:
            fileobj (BufferedReader): The tar file object to read from.
            shard_idx (int): The index of the shard.
            rank (int): The rank of the worker processing this shard.

        Yields:
            dict: A dictionary containing the aggregated data for each sample in the tar file.
        """
        tar = tarfile.open(fileobj=fileobj, mode=self.mode)

        seen_keys = set()
        aggregated_row = {
            "__wds_global_rank__": rank,
            "__wds_shard_idx__": shard_idx,
        }

        for member in self.tar_member_iterator(tar):
            if self.stop_event.is_set():
                break

            if member.isfile():
                extracted_file = tar.extractfile(member)
                if not extracted_file:
                    print("extracted file is none")
                    continue

                key, ext = os.path.splitext(member.name)
                prev_key = aggregated_row.get("__wds_sample_key__", None)

                if prev_key is not None and prev_key != key:
                    yield aggregated_row

                    aggregated_row = {
                        "__wds_global_rank__": rank,
                        "__wds_shard_idx__": shard_idx,
                    }

                    if key in seen_keys:
                        raise RuntimeError(
                            "Tarfile members are not sorted by keys. Aborting."
                        )
                    else:
                        seen_keys.add(key)

                aggregated_row["__wds_sample_key__"] = key
                aggregated_row[ext] = pa.py_buffer(extracted_file.read())

        if "__wds_sample_key__" in aggregated_row:
            yield aggregated_row

    def extract_shard(self, shard_idx: int, shard_key: str, rank: int):
        """
        Extract and process a single shard.

        This method extracts the contents of a shard, processes its files, and yields
        the aggregated data for each sample in the shard.

        Args:
            shard_idx (int): The index of the shard.
            shard_key (str): The key of the shard in the cache.
            rank (int): The rank of the worker processing this shard.

        Yields:
            dict: A dictionary containing the aggregated data for each sample in the shard.

        Raises:
            Exception: If the shard is not found in the cache.
        """
        with self.cache.with_shard_lock(shard_key) as acquired:
            if not acquired:
                logger.debug(f"Failed to acquire lock for shard {shard_key}. Skipping")
                yield None
                return

            try:
                file_path = self.cache.get_shard_path(shard_key, check_exists=True)
                if not file_path:
                    logger.error(f"Shard {shard_key} not found in cache")
                    raise Exception(f"Shard {shard_key} not found in cache")

                while (
                    pa.total_allocated_bytes() > self.memory_buffer_limit_bytes
                    and not self.stop_event.is_set()
                ):
                    logger.debug("Exceeded memory buffer quota. Sleeping for 1 seconds")
                    time.sleep(1)

                logger.debug(f"Extracting shard {shard_key} at {file_path}")
                with open(file_path, "rb") as f:
                    yield from self.tar_sample_iterator(
                        f, shard_idx=shard_idx, rank=rank
                    )

            except Exception as e:
                logger.error(f"Error extracting shard {shard_key}: {e}")
                import traceback

                logger.error(traceback.format_exc())

    def run_worker(self, rank: int):
        """
        Run the worker to process and extract shards.

        This method continuously processes shards from the input queue until the stop event is set
        or there are no more shards to process. It extracts samples from each shard and puts them
        into the output queue.

        Args:
            rank (int): The rank of the worker.
        """
        while not self.stop_event.is_set():
            if self.input_queue.empty() and self.input_finish_event.is_set():
                logger.debug("No more downloads to extract. Exiting")
                break

            try:
                shard_idx, shard_key = self.input_queue.get(block=False)
                for sample in self.extract_shard(shard_idx, shard_key, rank):
                    if sample is None:
                        print("Sample is None. Breaking...")
                        break

                    logger.debug(
                        f"Processed key {sample['__wds_sample_key__']} files from {shard_key}"
                    )
                    self.output_queue.put(sample)

                self.input_queue.task_done()

            except Empty:
                time.sleep(0.1)

    def run(self, num_threads: int, *, rank: int) -> None:
        """
        Run the extraction process with multiple worker threads.

        This method starts multiple worker threads to process and extract shards concurrently.
        It waits for all worker threads to complete before setting the output finish event.

        Args:
            num_threads (int): The number of worker threads to start.
            rank (int): The rank of the worker.
        """
        self.worker_threads = [
            threading.Thread(
                target=self.run_worker,
                args=(rank,),
            )
            for _ in range(num_threads)
        ]
        for worker in self.worker_threads:
            worker.start()

        for worker in self.worker_threads:
            worker.join()

        self.worker_threads = []
        self.output_finish_event.set()
