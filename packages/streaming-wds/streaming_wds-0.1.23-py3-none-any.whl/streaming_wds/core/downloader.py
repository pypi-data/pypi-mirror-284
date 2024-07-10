import logging
import threading
from queue import Empty, Queue
from typing import List, Optional
from urllib.parse import urlparse

from boto3 import Session
from botocore.config import Config

from .cache import LocalShardLRUCache
from .sharder import GetWorkerSplit, OrderByStride, Shuffle
from .types import WorkerInfo

logger = logging.getLogger(__name__)


AWS_DEFAULT_MAX_CONCURRENCY = 10


class DownloadCancelled(Exception):
    pass


def count_shards(remote: str, session: Session) -> List[str]:
    """
    Helper function to count the number of shards in a dataset outside of the ShardDownloader.

    Returns:
        List[str]: A list of shard keys.
    """
    s3 = session.client("s3")

    parsed_uri = urlparse(remote)
    bucket = parsed_uri.netloc
    key_prefix = parsed_uri.path.lstrip("/")

    shard_keys = []
    paginator = s3.get_paginator("list_objects_v2")
    for result in paginator.paginate(Bucket=bucket, Prefix=key_prefix):
        for content in result.get("Contents", []):
            if content["Key"].endswith(".tar"):
                shard_keys.append(content["Key"])

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

        parsed_uri = urlparse(remote)
        self.bucket = parsed_uri.netloc
        self.key_prefix = parsed_uri.path.lstrip("/")

        self.shards = self.find_shards()

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
        shard_keys = []
        paginator = self.s3.get_paginator("list_objects_v2")
        for result in paginator.paginate(Bucket=self.bucket, Prefix=self.key_prefix):
            for content in result.get("Contents", []):
                if content["Key"].endswith(".tar"):
                    shard_keys.append(content["Key"])

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
            self.cache.remove_shard(key)
            return False
        except Exception as e:
            logger.error(f"Error downloading shard {key}: {e}")
            self.cache.remove_shard(key)
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
            logger.debug(f"Shard {key} found in cache")
            return key

        logger.debug(f"Shard {key} not in cache, downloading")

        # Get file size
        response = self.s3.head_object(Bucket=self.bucket, Key=key)
        file_size = response["ContentLength"]
        shard_path = self.cache.add_shard(key, file_size)

        with self.cache.with_shard_lock(key) as acquired:
            if not acquired:
                logger.debug(f"Failed to acquire lock for shard {key}. Skipping")
                return None

            success = self.cancellable_download(key, shard_path)
            if success:
                return key
            else:
                return None

    def prefetch_shards(self, keys: List[str]):
        """
        Prefetch multiple shards in parallel.

        Args:
            keys (List[str]): List of S3 keys to prefetch.
        """
        # This is a placeholder for a more advanced prefetching mechanism
        # You could implement this using threads or asyncio for parallel downloads
        for key in keys:
            self.get_shard(key)

    def run(
        self,
        rank,
        worker_infos: List[WorkerInfo],
        epoch: int = 0,
        shuffle: bool = False,
    ):
        """
        Run the shard downloading process for a worker.

        Args:
            worker_info (WorkerInfo): Information about the worker.

        Raises:
            RuntimeError: If setup() was not called before run().
        """

        # Populate the download queue
        shards = self.shards
        worker_info = worker_infos[rank]

        if shuffle:
            shards = Shuffle.apply(shards, epoch)

        shards = OrderByStride.apply(shards, len(worker_infos))

        shards = GetWorkerSplit.apply(self.shards, worker_info)
        for shard in shards:
            self.input_queue.put(shard)

        # Download shards
        local_idx = 0
        while not self.stop_event.is_set():
            if self.input_queue.empty():
                break

            try:
                shard = self.input_queue.get(timeout=0.1)
                shard_idx = worker_info.start + local_idx

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
            except Empty:
                pass

        logger.debug("All shards downloaded. Exiting.")
        self.finish_event.set()
