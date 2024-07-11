import logging
import os
import threading
from queue import Empty, Queue
from typing import Any, Dict, Optional, Union

import boto3
import pyarrow as pa
from torch.utils.data import IterableDataset

from streaming_wds.core.index import DatasetIndex

from .core.cache import LocalShardLRUCache
from .core.downloader import (
    AWS_DEFAULT_MAX_CONCURRENCY,
    ShardDownloader,
    count_shards,
    load_index,
)
from .core.extractor import ShardExtractor
from .core.types import Bytes, WorkerInfoList
from .decoders import no_decoder, select_decoder
from .utils import (
    get_global_rank,
    get_mp_world_size,
)

logging.getLogger("botocore.configprovider").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


class StreamingWebDataset(IterableDataset):
    def __init__(
        self,
        remote: str,
        split: Optional[str] = None,
        profile: str = "default",
        shuffle: bool = False,
        max_workers: int = 2,
        schema: Dict[str, str] = {},
        memory_buffer_limit_bytes: Union[Bytes, int, str] = "2GB",
        file_cache_limit_bytes: Union[Bytes, int, str] = "2GB",
        tar_read_mode: str = "r|*",
    ):
        """
        Initialize the StreamingWebDataset.

        Args:
            remote (str): The S3 URI of the dataset.
            split (Optional[str], optional): The dataset split (e.g., "train", "val", "test"). Defaults to None.
            profile (str, optional): The AWS profile to use for authentication. Defaults to "default".
            drop_last (bool, optional): Whether to drop the last incomplete batch. Defaults to True.
            shuffle (bool, optional): Whether to shuffle the data. Defaults to False.
            max_workers (int, optional): Maximum number of worker threads for download and extraction. Defaults to 2.
            schema (Dict[str, str], optional): A dictionary defining the decoding method for each data field. Defaults to {}.
            memory_buffer_limit_bytes (int, optional): The maximum size of the memory buffer in bytes per worker. Defaults to 2GB.
            file_cache_limit_bytes (int, optional): The maximum size of the file cache in bytes per worker. Defaults to 2GB.
            tar_read_mode (Literal["r:*", "r|*"], optional): The mode for reading tar files. Defaults to "r|*" (streamed).
        """
        self.remote = os.path.join(remote, split) if split else remote
        self.shuffle = shuffle
        self.max_workers = max(2, (max_workers + 1) // 2 * 2)
        self.epoch = 0

        self.memory_buffer_limit_bytes = int(Bytes(memory_buffer_limit_bytes))
        self.file_cache_limit_bytes = int(Bytes(file_cache_limit_bytes))
        self.tar_read_mode = tar_read_mode

        if not schema:
            logger.warning("No schema provided. Decoding will be skipped.")
        self.decoders = {k: select_decoder(v) for (k, v) in schema.items()}

        self._session = boto3.Session(profile_name=profile)

        # We'll initialize the dataset assuming that there are no other dataset instances in the worker pool
        # The DataLoader will be responsible for setting the worker infos
        self._worker_infos: WorkerInfoList = WorkerInfoList.default(self.num_shards)
        self._worker_components_initialized = False

    @property
    def index(self) -> Optional[DatasetIndex]:
        """
        Get the index of the dataset.

        Returns:
            Optional[DatasetIndex]: The index of the dataset if it exists.
        """
        cache_dir = (
            self.cache.cache_dir if self._worker_components_initialized else None
        )
        index_file_path = os.path.join(cache_dir, "index_file") if cache_dir else None

        if cache_dir and os.path.exists(index_file_path):
            with open(index_file_path, "rb") as f:
                index_bytes = f.read()
            return DatasetIndex.decode(index_bytes)
        else:
            index = load_index(self.remote, self._session)
            if not index:
                return None
            if cache_dir:
                with open(index_file_path, "wb") as f:
                    f.write(index.encode())

    @property
    def num_shards(self):
        """
        Get the total number of shards in the dataset.

        Returns:
            int: The number of shards in the dataset.
        """
        return count_shards(self.remote, self._session)

    @property
    def num_samples(self) -> Optional[int]:
        """
        Get the total number of samples in the dataset.

        Returns:
            Optional[int]: The total number of samples in the dataset.
        """
        if self.index:
            return self.index.num_samples
        return None

    def set_epoch(self, epoch: int):
        """
        Set the epoch for the dataset.

        Args:
            epoch (int): The epoch to set.
        """
        self.epoch = epoch

    def set_worker_infos(self, worker_infos: WorkerInfoList):
        """
        Set the worker information for the dataset.

        Args:
            worker_infos (List[WorkerInfo]): A list of WorkerInfo objects containing information about each worker.
        """
        self._worker_infos = worker_infos

    def clear_worker_components(self):
        """
        Clear the worker components of the dataset.

        This method clears the worker components and sets the worker components initialized flag to False.
        """
        if self._worker_components_initialized:
            del self._download_queue
            del self._extract_queue
            del self._samples_queue

            del self._workers
            del self._stop_event
            del self._download_finished_event
            del self._dataset_finished_event

            del self.cache
            del self.downloader
            del self.extractor

        self._worker_components_initialized = False

    def prepare_worker_components(self):
        """
        Reset the worker components of the dataset.

        This method resets the global rank and reinitializes the worker components if they haven't been initialized before.
        If the components were already initialized, it empties the queues and resets the events.
        """
        self.reset_global_rank()

        if self._worker_components_initialized:
            self._stop_event.set()
            for worker in self._workers:
                if worker.is_alive():
                    logger.debug(
                        f"Found zombie workers on global_rank={self.global_rank}"
                    )
                    worker.join()

            # reset events
            self._stop_event.clear()
            self._download_finished_event.clear()
            self._dataset_finished_event.clear()
            return

        self._download_queue: Queue[str] = Queue()
        self._extract_queue: Queue[bytes] = Queue()
        self._samples_queue: Queue[Dict[str, bytes]] = Queue()

        self._workers = []
        self._stop_event = threading.Event()
        self._download_finished_event = threading.Event()
        self._dataset_finished_event = threading.Event()

        self.cache = LocalShardLRUCache(
            remote=self.remote,
            worker_rank=self.global_rank,
            cache_limit_bytes=self.file_cache_limit_bytes,
            stop_event=self._stop_event,
            overwrite=False,
        )
        self.downloader = ShardDownloader(
            remote=self.remote,
            session=self._session,
            input_queue=self._download_queue,
            output_queue=self._extract_queue,
            stop_event=self._stop_event,
            finish_event=self._download_finished_event,
            cache=self.cache,
            max_pool_connections=get_mp_world_size()
            * self.max_workers
            // 2
            * AWS_DEFAULT_MAX_CONCURRENCY,
        )
        self.extractor = ShardExtractor(
            input_queue=self._extract_queue,
            output_queue=self._samples_queue,
            stop_event=self._stop_event,
            input_finish_event=self._download_finished_event,
            output_finish_event=self._dataset_finished_event,
            cache=self.cache,
            memory_buffer_limit_bytes=self.memory_buffer_limit_bytes,
            mode=self.tar_read_mode,
        )

        self._worker_components_initialized = True

    def set_shuffle(self, shuffle: bool):
        """
        Set the shuffle parameter for the dataset.

        Args:
            shuffle (bool): Whether to shuffle the data or not.
        """
        self.shuffle = shuffle

    @property
    def global_rank(self):
        """
        Get the global rank of the current worker.

        Returns:
            int: The global rank of the current worker.
        """
        if not hasattr(self, "_cached_global_worker_rank"):
            self._cached_global_worker_rank = get_global_rank()
        return self._cached_global_worker_rank

    def reset_global_rank(self):
        """
        Reset the cached global rank of the current worker.
        """
        self._cached_global_worker_rank = get_global_rank()

    def _decode_sample(self, sample: Dict[str, bytes]) -> Dict[str, Any]:
        """
        Decode a sample using the specified decoders.

        Args:
            sample (Dict[str, bytes]): The sample to decode.

        Returns:
            Dict[str, Any]: The decoded sample.
        """
        decoded_sample = {}
        for key, value in sample.items():
            if isinstance(value, pa.Buffer):
                ref = value
                value = value.to_pybytes()
                del ref  # we've copied the memory, free it

            decoded_sample[key] = self.decoders.get(key, no_decoder)(value)
        return decoded_sample

    def process_sample(self, sample: Dict[str, bytes]) -> Dict[str, bytes]:
        """
        Process a sample before decoding.

        This method can be overridden to implement custom processing logic.

        Args:
            sample (Dict[str, bytes]): The sample to process.

        Returns:
            Dict[str, bytes]: The processed sample.
        """
        return sample

    def __iter__(self):
        """
        Create an iterator for the dataset.

        This method initializes the worker components, starts the worker threads,
        and yields processed samples from the dataset.

        Yields:
            Dict[str, Any]: Processed and decoded samples from the dataset.

        Raises:
            ValueError: If an internal key is reintroduced in the process_sample method.
            Exception: If an error occurs during iteration.
        """
        self.prepare_worker_components()

        self._workers = [
            threading.Thread(
                target=self.downloader.run,
                args=(self.max_workers // 2,),
                kwargs=dict(
                    rank=self.global_rank,
                    worker_infos=self._worker_infos,
                    epoch=self.epoch,
                    shuffle=self.shuffle,
                ),
            ),
            threading.Thread(
                target=self.extractor.run,
                args=(self.max_workers // 2,),
                kwargs=dict(rank=self.global_rank),
            ),
        ]

        for worker in self._workers:
            worker.start()

        try:
            while not self._stop_event.is_set():
                try:
                    sample = self._samples_queue.get(timeout=0.1)
                except Empty:
                    if self._dataset_finished_event.is_set():
                        break
                    continue

                sample = self._decode_sample(sample)

                # Extract internal keys
                internal_keys = {
                    "__wds_global_rank__": sample.pop("__wds_global_rank__", None),
                    "__wds_shard_idx__": sample.pop("__wds_shard_idx__", None),
                    "__wds_sample_key__": sample.pop("__wds_sample_key__", None),
                }

                # Process the sample
                sample = self.process_sample(sample)

                if isinstance(sample, dict):
                    # Check if internal keys were reintroduced
                    for key in internal_keys:
                        if key in sample:
                            raise ValueError(
                                f"Internal key '{key}' was reintroduced in process_sample method."
                            )

                    # Put back internal keys
                    sample.update(internal_keys)
                elif isinstance(sample, tuple):
                    sample = (
                        *sample,
                        internal_keys["__wds_global_rank__"],
                        internal_keys["__wds_shard_idx__"],
                        internal_keys["__wds_sample_key__"],
                    )
                else:
                    raise ValueError(
                        "The process_sample method must return a dictionary or a tuple."
                    )

                self._samples_queue.task_done()
                yield sample

        except Exception as e:
            logger.error(f"Error in dataset: {e}")
            raise

        finally:
            logger.debug(
                f"Cleaning up dataset worker components on global_rank={self.global_rank}"
            )
            self._stop_event.set()
            for worker in self._workers:
                worker.join()

    def __del__(self):
        """
        Clean up resources when the dataset object is deleted.

        This method stops all worker threads and deletes the cache.
        """
        if self._worker_components_initialized:
            self._stop_event.set()
            for worker in self._workers:
                worker.join()
            del self.cache
