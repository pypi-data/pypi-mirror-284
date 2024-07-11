import io
import logging
import os
import shutil
import tarfile
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager
from pathlib import Path
from queue import Queue
from typing import Generator, Optional, Tuple
from urllib.parse import urlparse

import torch
import torch.distributed as dist
from boto3 import Session
from filelock import FileLock, Timeout
from tenacity import retry, stop_after_attempt, wait_exponential
from tensordict import TensorDict
from tqdm import tqdm

from .core.index import DatasetIndex, ShardIndex

logger = logging.getLogger(__name__)


@contextmanager
def isolate_torch_rng() -> Generator[None, None, None]:
    """A context manager that resets the torch global random state on exit to what it was before entering.

    Example:
        >>> import torch
        >>> torch.manual_seed(1)  # doctest: +ELLIPSIS
        <torch._C.Generator object at ...>
        >>> with isolate_rng():
        ...     [torch.rand(1) for _ in range(3)]
        [tensor([0.7576]), tensor([0.2793]), tensor([0.4031])]
        >>> torch.rand(1)
        tensor([0.7576])

    """
    torch_state = torch.get_rng_state()
    try:
        yield
    finally:
        torch.set_rng_state(torch_state)


def get_global_world_size() -> int:
    """
    Get the total number of workers across all distributed processes and data loader workers.

    Returns:
        int: The global world size, which is the product of the distributed world size
             and the number of data loader workers.
    """
    curr_mp_world_size = (
        torch.utils.data.get_worker_info().num_workers
        if torch.utils.data.get_worker_info()
        else 1
    )
    if dist.is_initialized():
        return dist.get_world_size() * curr_mp_world_size
    return curr_mp_world_size


def get_dist_world_size() -> int:
    """
    Get the number of processes in the distributed training setup.

    Returns:
        int: The number of distributed processes if distributed training is initialized,
             otherwise 1.
    """
    if dist.is_initialized():
        return dist.get_world_size()
    return 1


def get_mp_world_size() -> int:
    """
    Get the number of worker processes for the current DataLoader.

    Returns:
        int: The number of worker processes if running in a DataLoader worker,
             otherwise 1.
    """
    return (
        torch.utils.data.get_worker_info().num_workers
        if torch.utils.data.get_worker_info()
        else 1
    )


def get_dist_rank() -> int:
    """
    Get the rank of the current process in the distributed training setup.

    Returns:
        int: The rank of the current process if distributed training is initialized,
             otherwise 0.
    """
    if dist.is_initialized():
        return int(dist.get_rank())
    return 0


def get_mp_rank() -> int:
    """
    Get the rank of the current DataLoader worker process.

    Returns:
        int: The rank of the current DataLoader worker if running in a worker process,
             otherwise 0.
    """
    return (
        torch.utils.data.get_worker_info().id
        if torch.utils.data.get_worker_info()
        else 0
    )


def get_global_rank() -> int:
    """
    Get the global rank of the current process, considering both distributed training
    and DataLoader workers.

    Returns:
        int: The global rank of the current process.
    """
    curr_mp_world_size = get_mp_world_size()
    curr_mp_rank = get_mp_rank()
    curr_dist_rank = get_dist_rank()

    return curr_dist_rank * curr_mp_world_size + curr_mp_rank


def update_global_tensordict(
    global_dict: TensorDict, local_dict: TensorDict
) -> TensorDict:
    """
    Update the global TensorDict with values from the local TensorDict.

    This function updates the global TensorDict with the values from the local TensorDict.
    It's typically used in distributed settings to synchronize data across processes.

    Args:
        global_dict (TensorDict): The global TensorDict to be updated.
        local_dict (TensorDict): The local TensorDict containing the updates.

    Returns:
        TensorDict: The updated global TensorDict.

    Note:
        This function modifies the global_dict in-place and also returns it.
    """
    return global_dict.update(local_dict)


def empty_queue(queue: Queue):
    """
    Empty a queue by removing and discarding all its items.

    Args:
        queue (Queue): The queue to be emptied.
    """
    while not queue.empty():
        try:
            queue.get_nowait()
        except Exception:
            pass
        queue.task_done()


def parse_uri(uri: str) -> Tuple[str, str]:
    """
    Parse a URI into a bucket and key.

    Args:
        uri (str): The URI to be parsed.

    Returns:
        Tuple[str, str]: A tuple containing the bucket and key parsed from the URI.
    """
    parsed_uri = urlparse(uri)
    bucket = parsed_uri.netloc
    key = parsed_uri.path.lstrip("/")
    return bucket, key


@contextmanager
def cache_lock(remote: str, split: Optional[str] = None, rank: Optional[int] = None):
    """
    A context manager that uses a file lock to ensure the code within is executed only once.

    This function creates a lock file based on the remote URL and split, and attempts to acquire
    a lock on this file. If successful, it yields True, indicating that the calling process
    should execute the code within the context. If unsuccessful, it yields False, indicating
    that the calling process should skip the code within the context.

    Args:
        remote (str): The remote URL of the dataset.
        split (Optional[str]): The split name of the dataset, if applicable.

    Yields:
        bool: True if the lock was acquired (indicating the process should execute the code),
              False otherwise.

    Example:
        with cache_lock("https://example.com/data", "train") as acquired:
            if acquired:
                # This code will only be executed by one process
                download_and_process_data()
    """
    if split:
        remote = os.path.join(remote, split)
    if rank is not None:
        remote = os.path.join(remote, str(rank))

    bucket, key_prefix = parse_uri(remote)
    lock_file = Path.home() / ".cache" / "streaming_wds" / f"{bucket}_{key_prefix}.lock"

    lock_file.parent.mkdir(parents=True, exist_ok=True)
    lock = FileLock(str(lock_file))

    try:
        with lock.acquire(timeout=1):
            yield True  # Lock acquired, this process should handle the code within the context
            if rank is None:
                # Ensure the lock is held for a minimum duration
                time.sleep(5)
    except Timeout:
        yield False  # Lock not acquired, this process should not handle the code within the context
    finally:
        if lock_file.exists():
            try:
                lock_file.unlink()  # Remove the lock file
            except OSError:
                pass  # Ignore errors if the file can't be removed


def clean_stale_cache(remote: str, split: Optional[str] = None):
    """
    Clear stale caches for a specific remote and split.

    This function deletes the cache directory for the given remote and split.

    Args:
        remote (str): The remote URL of the dataset.
        split (str): The split name of the dataset.

    Returns:
        bool: True if the cache was successfully cleared, False otherwise.
    """

    with cache_lock(remote, split):
        if split is not None:
            remote = os.path.join(remote, split)

        bucket, key_prefix = parse_uri(remote)
        cache_dir = Path.home() / ".cache" / "streaming_wds" / bucket / key_prefix

        if cache_dir.exists():
            try:
                shutil.rmtree(cache_dir)
                logger.info(f"Cleared cache for remote {remote} at {cache_dir}")
            except OSError:
                pass
        else:
            logger.info(f"No cache found for remote {remote} at {cache_dir}")


@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    reraise=True,
)
def compute_shard_index(bucket: str, shard_key: str, session: Session) -> ShardIndex:
    """
    Compute the index for a single shard in an S3 bucket.

    This function retrieves a tar file from S3, reads its contents, and computes
    the number of samples in the shard. It uses retry logic to handle potential
    transient errors when interacting with S3.

    Args:
        bucket (str): The name of the S3 bucket containing the shard.
        shard_key (str): The key (path) of the shard file in the S3 bucket.
        session (Session): An authenticated boto3 Session object for S3 access.

    Returns:
        ShardIndex: An object containing the shard key and the number of samples in the shard.

    Raises:
        Any exceptions from S3 operations or file processing that persist after retries.
    """
    s3 = session.client("s3")

    response = s3.get_object(Bucket=bucket, Key=shard_key)
    tar_content = response["Body"].read()

    tar_file_like = io.BytesIO(tar_content)
    sample_keys = set()

    with tarfile.open(fileobj=tar_file_like, mode="r") as tar:
        for member in tar:
            if member.isfile():
                key, _ = os.path.splitext(member.name)
                sample_keys.add(key)

    # Create and return the ShardIndex
    return ShardIndex(key=shard_key, num_samples=len(sample_keys))


def compute_dataset_index(
    remote: str,
    split: Optional[str] = None,
    profile: Optional[str] = None,
    write: bool = False,
):
    """
    Compute the index for a dataset stored in S3.

    This function calculates the index for a dataset by processing all shards
    in the specified S3 location. It counts the number of shards and items,
    and optionally writes the index back to S3.

    Args:
        remote (str): The S3 URI of the dataset.
        split (Optional[str]): The dataset split to process. If provided,
            it will be appended to the remote path.
        profile (Optional[str]): The AWS profile name to use for authentication.
        write (bool): If True, write the computed index back to S3.

    Returns:
        DatasetIndex: An object containing the computed index information.

    Raises:
        ValueError: If no shards are found in the specified location.
    """
    if split:
        remote = os.path.join(remote, split)

    index = DatasetIndex(num_shards=0, num_items=0, shards=[])

    session = Session(profile_name=profile)
    s3 = session.client("s3")
    bucket, key_prefix = parse_uri(remote)

    # Find the shard keys
    shard_keys = []
    paginator = s3.get_paginator("list_objects_v2")
    for result in paginator.paginate(Bucket=bucket, Prefix=key_prefix):
        for content in result.get("Contents", []):
            if content["Key"].endswith(".tar"):
                shard_keys.append(content["Key"])

    if not shard_keys:
        raise ValueError(f"No shards found in {remote}")

    index.num_shards = len(shard_keys)
    print(f"Found {index.num_shards} shards in {remote}")

    # Count the number of items in each shard
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(compute_shard_index, bucket, key, session)
            for key in shard_keys
        ]

        shard_indices = []
        for future in tqdm(
            as_completed(futures), total=len(futures), desc="Processing shards"
        ):
            try:
                shard_index = future.result()
                shard_indices.append(shard_index)
                index.num_items += shard_index.num_samples
            except Exception as exc:
                print(f"A shard generated an exception: {exc}")

    index.shards = shard_indices

    if write:
        index_bytes = index.encode()
        s3.put_object(Bucket=bucket, Key=f"{key_prefix}/index.wds", Body=index_bytes)

    return index
