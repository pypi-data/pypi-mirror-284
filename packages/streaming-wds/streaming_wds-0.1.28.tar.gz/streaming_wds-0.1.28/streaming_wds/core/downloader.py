import logging
import os
import threading
from queue import Queue
from typing import List, Optional

from boto3 import Session
from botocore.config import Config

from streaming_wds.core.index import DatasetIndex
from streaming_wds.utils import parse_uri

from .cache import LocalShardLRUCache
from .sharder import GetWorkerSplit, OrderByStride, Shuffle
from .types import WorkerInfo, WorkerInfoList

logger = logging.getLogger(__name__)


AWS_DEFAULT_MAX_CONCURRENCY = 10


class DownloadCancelled(Exception):
    pass


def iterate_tarfiles(bucket, key_prefix, s3_client):
    """
    Helper function to iterate over all .tar files in a bucket, including compressed variants.

    Args:
        bucket (str): The S3 bucket name.
        key_prefix (str): The prefix for S3 keys.
        session (Session): The boto3 session.

    Returns:
        Iterator[str]: An iterator over the keys.
    """
    paginator = s3_client.get_paginator("list_objects_v2")
    for result in paginator.paginate(Bucket=bucket, Prefix=key_prefix):
        for content in result.get("Contents", []):
            if (
                content["Key"].lower().endswith(".tar")
                or ".tar." in content["Key"].lower()
            ):
                yield content["Key"]


def load_index(bucket, key_prefix, s3_client) -> DatasetIndex:
    """
    Load the dataset index from an S3 bucket.

    This function attempts to retrieve and decode the dataset index file
    from the specified S3 bucket and key prefix. The index file is expected
    to be named 'index.wds'.

    Args:
        bucket (str): The name of the S3 bucket.
        key_prefix (str): The prefix for the S3 keys.
        s3_client (boto3.client): The S3 client used to interact with the S3 service.

    Returns:
        DatasetIndex: The decoded dataset index.
        If the index file does not exist, returns None.
    """
    index_key = os.path.join(key_prefix, "index.wds")

    try:
        response = s3_client.get_object(Bucket=bucket, Key=index_key)
        file_bytes = response["Body"].read()
        return DatasetIndex.decode(file_bytes)
    except s3_client.exceptions.NoSuchKey:
        return None


def count_shards(remote: str, session: Session) -> int:
    """
    Helper function to count the number of shards in a dataset outside of the ShardDownloader.

    Returns:
        int: The number of shards.
    """
    s3 = session.client("s3")
    bucket, key_prefix = parse_uri(remote)

    cached_index = load_index(bucket, key_prefix, s3)
    if cached_index is not None:
        return cached_index.num_shards

    shard_keys = list(iterate_tarfiles(bucket, key_prefix, s3))
    return len(shard_keys)


class ShardDownloader:
    """
    A class for downloading shards from S3 and managing the download process.

    This class handles the downloading of shards from S3, caching them locally,
    and managing the download queue for multiple workers.

    Attributes:
        s3 (boto3.client): The S3 client for interacting with AWS S3.
        shards (Optional[List[str]]): List of shard keys to be downloaded.
        cache (LocalShardLRUCache): Local cache for storing downloaded shards.
        input_queue (Queue): Queue for incoming shard download requests.
        output_queue (Queue): Queue for outputting downloaded shard information.
        stop_event (threading.Event): Event to signal stopping of the download process.
        finish_event (threading.Event): Event to signal completion of downloads.
        bucket (str): The S3 bucket name.
        key_prefix (str): The prefix for S3 keys.
    """

    def __init__(
        self,
        *,
        remote: str,
        session: Session,
        input_queue: Queue,
        output_queue: Queue,
        stop_event: threading.Event,
        finish_event: threading.Event,
        cache: LocalShardLRUCache,
        max_attempts: int = 10,
        max_pool_connections: int = 10,
    ):
        """
        Initialize the ShardDownloader.

        Args:
            remote (str): The remote S3 uri.
            session (Session): The boto3 session.
            input_queue (Queue): Queue for incoming shard download requests.
            output_queue (Queue): Queue for outputting downloaded shard information.
            stop_event (threading.Event): Event to signal stopping of the download process.
            finish_event (threading.Event): Event to signal completion of downloads.
            cache (LocalShardLRUCache): Local cache for storing downloaded shards.
        """
        self.s3 = session.client(
            "s3",
            config=Config(
                retries={"max_attempts": max_attempts},
                max_pool_connections=max_pool_connections,
            ),
        )
        self.shards: Optional[List[str]] = None
        self.cache = cache

        self.input_queue = input_queue
        self.output_queue = output_queue
        self.stop_event = stop_event
        self.finish_event = finish_event

        self.bucket, self.key_prefix = parse_uri(remote)
        self.shards = self.find_shards()
        self.worker_threads = []

    def set_queues(self, *, input_queue: Queue, output_queue: Queue):
        """
        Set the input and output queues for the downloader.

        Args:
            input_queue (Queue): Queue for incoming shard extraction requests.
            output_queue (Queue): Queue for outputting extracted samples.
        """
        self.input_queue = input_queue
        self.output_queue = output_queue

    def num_shards(self):
        """
        Get the number of shards.

        Returns:
            int: The number of shards.
        """
        if self.shards is not None:
            return len(self.shards)

        elif not hasattr(self, "_cached_num_shards"):
            self._cached_num_shards = len(self.find_shards())

        return self._cached_num_shards

    def find_shards(self):
        """
        Find all shards in the S3 bucket with the given prefix.

        Returns:
            List[str]: A list of shard keys.
        """
        cached_index = load_index(self.bucket, self.key_prefix, self.s3)
        if cached_index:
            logger.debug(
                f"Retrieving shard_keys from DatasetIndex for {self.bucket}/{self.key_prefix}"
            )
            return cached_index.shard_keys

        shard_keys = list(iterate_tarfiles(self.bucket, self.key_prefix, self.s3))
        return shard_keys

    def download_cancel_helper(self, _: int) -> None:
        """
        Helper function to check if download should be cancelled.

        Args:
            _ (int): Unused parameter, typically represents bytes transferred.

        Raises:
            DownloadCancelled: If the stop event is set.
        """
        if self.stop_event.is_set():
            raise DownloadCancelled()

    def cancellable_download(self, key: str, output_path: str) -> bool:
        """
        Download a file from S3 with the ability to cancel the download.

        Args:
            key (str): The S3 key of the file to download.
            output_path (str): The local path to save the downloaded file.

        Returns:
            bool: True if download was successful, False otherwise.

        Raises:
            Exception: Any unexpected error during download.
        """
        try:
            self.s3.download_file(
                Bucket=self.bucket,
                Key=key,
                Filename=output_path,
                Callback=self.download_cancel_helper,
            )
            return True
        except DownloadCancelled:
            logger.debug(f"Download of {key} was cancelled")
            return False
        except Exception as e:
            logger.error(f"Error downloading shard {key}: {e}")
            return False

    def get_shard(self, key: str) -> str:
        """
        Get the shard from the cache if it exists, otherwise download it.

        Args:
            key (str): The S3 key of the shard.

        Returns:
            str: The local path to the shard file, or None if download failed.
        """
        cached_path = self.cache.get_shard(key)
        if cached_path:
            logger.debug(f"[{self.cache.worker_rank}] Shard {key} found in cache")
            return key

        logger.debug(
            f"[{self.cache.worker_rank}] Shard {key} not in cache, downloading"
        )

        # Get file size
        response = self.s3.head_object(Bucket=self.bucket, Key=key)
        file_size = response["ContentLength"]

        shard_path = self.cache.add_shard(key, file_size)
        if shard_path is None:
            return

        with self.cache.with_shard_lock(key):
            success = self.cancellable_download(key, shard_path)

        if not success:
            self.cache.remove_shard(key)
            return None

        return key

    def populate_input_queue(
        self, rank, worker_infos: WorkerInfoList, epoch: int = 0, shuffle: bool = False
    ):
        """
        Populate the download queue with shards assigned to the worker.

        This method assigns shards to the worker based on the rank and worker information.
        It can also shuffle the shards if specified.

        Args:
            rank (int): The rank of the worker.
            worker_infos (WorkerInfoList): List of worker information.
            epoch (int, optional): The current epoch for shuffling. Defaults to 0.
            shuffle (bool, optional): Whether to shuffle the shards. Defaults to False.
        """
        shards = self.shards
        worker_info = worker_infos[rank]

        if shuffle:
            shards = Shuffle.apply(shards, epoch)

        shards = OrderByStride.apply(shards, len(worker_infos))
        shards = GetWorkerSplit.apply(self.shards, worker_info)

        for local_idx, shard in enumerate(shards):
            self.input_queue.put((local_idx, shard))

    def run_worker(
        self,
        worker_info: WorkerInfo,
    ) -> None:
        """
        Run the worker to download shards.

        This method continuously processes shards from the input queue until the stop event is set
        or there are no more shards to process. It downloads each shard and puts them into the output queue.

        Args:
            worker_info (WorkerInfo): Information about the worker.
        """
        while True:
            local_idx, shard = self.input_queue.get()
            shard_idx = worker_info.idx + local_idx

            if self.stop_event.is_set():
                logger.debug("Stopping worker")
                self.input_queue.task_done()
                continue

            # Shard-level mid-epoch resumption
            if worker_info.resume and shard_idx < worker_info.idx:
                logger.debug(f"Skipping shard {shard} as it was already processed")
                self.input_queue.task_done()
                continue

            # Download the shard
            shard = self.get_shard(shard)
            if shard:
                self.output_queue.put((shard_idx, shard))
            else:
                logger.debug(f"Failed to download shard: {shard}")

            self.input_queue.task_done()

    def run(
        self,
        num_threads: int,
        *,
        rank,
        worker_infos: WorkerInfoList,
        epoch: int,
        shuffle: bool,
    ) -> None:
        """
        Run the download process with multiple worker threads.

        This method starts multiple worker threads to download shards concurrently.
        It waits for all worker threads to complete before setting the finish event.

        Args:
            num_threads (int): The number of worker threads to start.
            worker_info (WorkerInfo): Information about the worker.
        """
        self.populate_input_queue(rank, worker_infos, epoch, shuffle)

        worker_info = worker_infos[rank]
        self.worker_threads = [
            threading.Thread(
                target=self.run_worker,
                args=(worker_info,),
                daemon=True,
            )
            for _ in range(num_threads)
        ]
        for worker in self.worker_threads:
            worker.start()

        self.input_queue.join()
        self.finish_event.set()
        self.worker_threads = []
