import logging
import os
import shutil
import threading
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Optional
from urllib.parse import urlparse

from streaming_wds.utils import cache_lock

logger = logging.getLogger(__name__)


class LocalShardLRUCache:
    """
    A local cache for shards using a Least Recently Used (LRU) eviction policy.

    This class manages a local cache of shards, handling their storage, retrieval,
    and eviction based on a size limit and access patterns.

    Attributes:
        remote (str): The remote uri of the dataset.
        bucket (str): The bucket name extracted from the remote uri.
        key_prefix (str): The key prefix extracted from the remote uri.
        cache_dir (Path): The local directory where shards are cached.
        cache_limit_bytes (int): The maximum size of the cache in bytes.
        current_cache_size (int): The current size of the cache in bytes.
        cache_lock (threading.Lock): A lock for thread-safe cache operations.
        shard_locks (Dict[str, threading.Lock]): Locks for individual shards.
        shard_access_times (Dict[str, int]): Last access times for shards.
        shard_read_count (Dict[str, int]): Read counts for shards.
    """

    def __init__(
        self,
        *,
        remote: str,
        worker_rank: int,
        cache_limit_bytes: int,
        stop_event: threading.Event,
        overwrite: bool = False,
    ):
        """
        Initialize the LocalShardLRUCache.

        Args:
            remote (str): The remote URL of the dataset.
            worker_rank (int): The rank of the worker using this cache.
            cache_limit_bytes (int): The maximum size of the cache in bytes.
        """
        self.remote = remote
        self.worker_rank = worker_rank

        parsed_uri = urlparse(self.remote)
        self.bucket = parsed_uri.netloc
        self.key_prefix = parsed_uri.path.lstrip("/")
        self.overwrite = overwrite
        self.stop_event = stop_event

        self.cache_dir = (
            Path.home()
            / ".cache"
            / "streaming_wds"
            / self.bucket
            / self.key_prefix
            / str(worker_rank)
        )
        self.cache_limit_bytes = cache_limit_bytes
        self.current_cache_size = 0

        self._cache_lock = threading.Lock()

        self.shard_locks: Dict[str, threading.Lock] = {}
        self.shard_access_times: Dict[str, int] = {}
        self.shard_read_count: Dict[str, int] = {}

        self.lock_file = self.cache_dir / ".cache_lock"
        self.create_lock_file()
        self.load_cache()

    def clear_partial_cache(self):
        """
        Clear any partially downloaded files in the cache, including those in subdirectories.
        """
        with cache_lock(self.remote, rank=self.worker_rank):
            with self.with_cache_lock() as acquired:
                if not acquired:
                    return

                # Get all files in the cache directory and its subdirectories
                all_files = list(self.cache_dir.glob("**/*.tar*"))

                # Group files by their prefix (everything up until the second dot if it exists) and relative path
                file_groups = {}
                for file in all_files:
                    if file.is_file():
                        relative_path = file.relative_to(self.cache_dir)
                        name_parts = relative_path.name.split(".", 2)
                        prefix = relative_path.with_name(
                            ".".join(name_parts[:2])
                            if len(name_parts) > 2
                            else name_parts[0]
                        )
                        if prefix not in file_groups:
                            file_groups[prefix] = []
                        file_groups[prefix].append(file)

                for prefix, files in file_groups.items():
                    # Check if there's more than one file with this prefix
                    if len(files) > 1:
                        shard_key = str(self.key_prefix / prefix)
                        logger.debug(
                            f"Found partial download for shard {shard_key}. Removing."
                        )

                        for file in files:
                            try:
                                file.unlink()
                            except FileNotFoundError:
                                pass

                        # Remove the shard from locks and tracking dictionaries
                        self.shard_locks.pop(shard_key, None)
                        self.shard_access_times.pop(shard_key, None)
                        self.shard_read_count.pop(shard_key, None)

                        # Update the current cache size
                        self.current_cache_size -= file.stat().st_size

    def create_lock_file(self):
        """
        Create a lock file to prevent other processes from modifying the cache.
        If the lock file already exists, raise an exception.
        """
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        if self.lock_file.exists() and not self.overwrite:
            raise RuntimeError(
                f"Cache at {self.cache_dir} is already in use by another process."
            )

        with open(self.lock_file, "w") as f:
            f.write(str(os.getpid()))

    def free_lock_file(self):
        """
        Remove the lock file to allow other processes to modify the cache.
        """
        if self.lock_file.exists():
            self.lock_file.unlink()

    def load_cache(self) -> None:
        """
        Load the cache, clearing existing content if present.

        This method ensures the cache directory exists and is empty.
        """
        if self.cache_dir.exists():
            # Only remove contents, not the directory itself or the lock file
            for item in self.cache_dir.iterdir():
                if item != self.lock_file:
                    if item.is_file():
                        item.unlink()
                    elif item.is_dir():
                        shutil.rmtree(item)
        else:
            self.cache_dir.mkdir(parents=True, exist_ok=True)

    def __del__(self):
        self.free_lock_file()

    def get_shard_path(self, shard_key: str, check_exists: bool = False) -> str:
        """
        Get the local path for a shard.

        Args:
            shard_key (str): The key of the shard.
            check_exists (bool): If True, return None if the shard doesn't exist.

        Returns:
            str: The local path of the shard, or None if check_exists is True and the shard doesn't exist.
        """
        shard_path = self.cache_dir / shard_key.replace(self.key_prefix, "").lstrip("/")
        shard_path.parent.mkdir(parents=True, exist_ok=True)
        if check_exists and not shard_path.exists():
            return None
        return shard_path

    def get_shard(self, shard_key: str) -> Optional[str]:
        """
        Get a shard from the cache.

        This method updates the access time and read count for the shard.

        Args:
            shard_key (str): The key of the shard to retrieve.

        Returns:
            Optional[str]: The path to the shard if it exists in the cache, None otherwise.
        """
        with self.with_cache_lock() as acquired:
            if not acquired:
                return None

            shard_path = self.get_shard_path(shard_key)
            if shard_path.exists():
                self.shard_access_times[shard_key] = time.time()

                if shard_key not in self.shard_locks:
                    self.shard_locks[shard_key] = threading.Lock()

                if shard_key not in self.shard_access_times:
                    self.shard_access_times[shard_key] = time.time()

                if shard_key not in self.shard_read_count:
                    self.shard_read_count[shard_key] = 0
                return str(shard_path)
            return None

    @contextmanager
    def with_cache_lock(self):
        """
        Acquire the cache lock for the duration of a context manager.

        Yields:
            bool: True if the lock was acquired, False if the lock is already held.
        """
        while not self.stop_event.is_set():
            acquired = self._cache_lock.acquire(timeout=0.1)
            if acquired:
                try:
                    yield True
                finally:
                    self._cache_lock.release()
                return
        yield False

    @contextmanager
    def with_shard_lock(self, shard_key: str):
        """
        Acquire the lock for a specific shard for the duration of a context manager.

        Args:
            shard_key (str): The key of the shard to lock.

        Yields:
            bool: True if the lock was acquired, False if the shard doesn't exist.
        """
        with self.with_cache_lock() as acquired:
            if not acquired:
                yield False
                return

            shard_lock = self.shard_locks.get(shard_key, None)
            if shard_lock is None:
                raise ValueError(f"Shard {shard_key} does not exist in the cache.")

        while not self.stop_event.is_set():
            if shard_lock.acquire(timeout=0.1):
                try:
                    yield True
                finally:
                    shard_lock.release()
                    with self.with_cache_lock():
                        self.shard_read_count[shard_key] += 1
                return

        # If we exit the loop due to stop_event being set
        yield False

    def add_shard(self, shard_key: str, shard_size: int):
        """
        Add a new shard to the cache.

        If there's not enough space, this method will evict old shards until there's room.

        Args:
            shard_key (str): The key of the shard to add.
            shard_size (int): The size of the shard in bytes.

        Returns:
            str: The path where the shard should be stored.
        """
        while not self.stop_event.is_set():
            with self.with_cache_lock():
                if self.current_cache_size + shard_size <= self.cache_limit_bytes:
                    self.current_cache_size += shard_size
                    self.shard_access_times[shard_key] = time.time()
                    self.shard_locks[shard_key] = threading.Lock()
                    self.shard_read_count[shard_key] = 0  # Initialize read count
                    return self.get_shard_path(shard_key)

            self._evict_oldest_shard()

    def remove_shard(self, shard_key: str):
        """
        Remove a shard from the cache.

        Args:
            shard_key (str): The key of the shard to remove.
        """
        with self.with_cache_lock() as acquired:
            if not acquired:
                return

            shard_path = self.get_shard_path(shard_key)
            if shard_path.exists():
                shard_size = shard_path.stat().st_size
                with self.with_shard_lock(shard_key):
                    self.current_cache_size -= shard_size

                # Remove the shard and any part files
                shard_prefix = str(shard_path).rstrip(".tar")
                for file in os.listdir(os.path.dirname(shard_path)):
                    if file.startswith(os.path.basename(shard_prefix)):
                        try:
                            os.remove(os.path.join(os.path.dirname(shard_path), file))
                        except FileNotFoundError:
                            pass

    def _evict_oldest_shard(self) -> None:
        """
        Evict the oldest shard from the cache.

        This method removes the least recently used shard that has been read more than once.
        If no such shard exists, it waits and tries again.
        """
        logger.debug("Evicting oldest shard from cache")
        while not self.stop_event.is_set():
            eligible_shards = [
                shard
                for shard in self.shard_access_times
                if self.shard_read_count.get(shard, 0) > 1
            ]

            if not eligible_shards:
                time.sleep(0.1)
                continue

            oldest_shard = min(eligible_shards, key=self.shard_access_times.get)
            shard_path = self.get_shard_path(oldest_shard)
            shard_size = shard_path.stat().st_size

            with self.with_cache_lock():
                with self.with_shard_lock(oldest_shard):
                    self.current_cache_size -= shard_size
                del self.shard_access_times[oldest_shard]
                del self.shard_locks[oldest_shard]
                del self.shard_read_count[oldest_shard]

            logger.debug(f"Evicting shard {oldest_shard} from cache")
            os.remove(shard_path)
