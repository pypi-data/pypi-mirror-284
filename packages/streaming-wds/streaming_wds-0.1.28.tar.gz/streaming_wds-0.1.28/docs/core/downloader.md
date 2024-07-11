# Downloader

[Streaming-wds Index](../README.md#streaming-wds-index) / [Core](./index.md#core) / Downloader

> Auto-generated documentation for [core.downloader](../../streaming_wds/core/downloader.py) module.

- [Downloader](#downloader)
  - [DownloadCancelled](#downloadcancelled)
  - [ShardDownloader](#sharddownloader)
    - [ShardDownloader().cancellable_download](#sharddownloader()cancellable_download)
    - [ShardDownloader().download_cancel_helper](#sharddownloader()download_cancel_helper)
    - [ShardDownloader().find_shards](#sharddownloader()find_shards)
    - [ShardDownloader().get_shard](#sharddownloader()get_shard)
    - [ShardDownloader().num_shards](#sharddownloader()num_shards)
    - [ShardDownloader().populate_input_queue](#sharddownloader()populate_input_queue)
    - [ShardDownloader().run](#sharddownloader()run)
    - [ShardDownloader().run_worker](#sharddownloader()run_worker)
    - [ShardDownloader().set_queues](#sharddownloader()set_queues)
  - [count_shards](#count_shards)
  - [iterate_tarfiles](#iterate_tarfiles)
  - [load_index](#load_index)

## DownloadCancelled

[Show source in downloader.py:23](../../streaming_wds/core/downloader.py#L23)

#### Signature

```python
class DownloadCancelled(Exception): ...
```



## ShardDownloader

[Show source in downloader.py:94](../../streaming_wds/core/downloader.py#L94)

A class for downloading shards from S3 and managing the download process.

This class handles the downloading of shards from S3, caching them locally,
and managing the download queue for multiple workers.

#### Attributes

- `s3` *boto3.client* - The S3 client for interacting with AWS S3.
- `shards` *Optional[List[str]]* - List of shard keys to be downloaded.
- `cache` *LocalShardLRUCache* - Local cache for storing downloaded shards.
- `input_queue` *Queue* - Queue for incoming shard download requests.
- `output_queue` *Queue* - Queue for outputting downloaded shard information.
- `stop_event` *threading.Event* - Event to signal stopping of the download process.
- `finish_event` *threading.Event* - Event to signal completion of downloads.
- `bucket` *str* - The S3 bucket name.
- `key_prefix` *str* - The prefix for S3 keys.

#### Signature

```python
class ShardDownloader:
    def __init__(
        self,
        remote: str,
        session: Session,
        input_queue: Queue,
        output_queue: Queue,
        stop_event: threading.Event,
        finish_event: threading.Event,
        cache: LocalShardLRUCache,
        max_attempts: int = 10,
        max_pool_connections: int = 10,
    ): ...
```

### ShardDownloader().cancellable_download

[Show source in downloader.py:213](../../streaming_wds/core/downloader.py#L213)

Download a file from S3 with the ability to cancel the download.

#### Arguments

- `key` *str* - The S3 key of the file to download.
- `output_path` *str* - The local path to save the downloaded file.

#### Returns

- `bool` - True if download was successful, False otherwise.

#### Raises

- `Exception` - Any unexpected error during download.

#### Signature

```python
def cancellable_download(self, key: str, output_path: str) -> bool: ...
```

### ShardDownloader().download_cancel_helper

[Show source in downloader.py:200](../../streaming_wds/core/downloader.py#L200)

Helper function to check if download should be cancelled.

#### Arguments

- `_` *int* - Unused parameter, typically represents bytes transferred.

#### Raises

- [DownloadCancelled](#downloadcancelled) - If the stop event is set.

#### Signature

```python
def download_cancel_helper(self, _: int) -> None: ...
```

### ShardDownloader().find_shards

[Show source in downloader.py:183](../../streaming_wds/core/downloader.py#L183)

Find all shards in the S3 bucket with the given prefix.

#### Returns

- `List[str]` - A list of shard keys.

#### Signature

```python
def find_shards(self): ...
```

### ShardDownloader().get_shard

[Show source in downloader.py:242](../../streaming_wds/core/downloader.py#L242)

Get the shard from the cache if it exists, otherwise download it.

#### Arguments

- `key` *str* - The S3 key of the shard.

#### Returns

- `str` - The local path to the shard file, or None if download failed.

#### Signature

```python
def get_shard(self, key: str) -> str: ...
```

### ShardDownloader().num_shards

[Show source in downloader.py:168](../../streaming_wds/core/downloader.py#L168)

Get the number of shards.

#### Returns

- `int` - The number of shards.

#### Signature

```python
def num_shards(self): ...
```

### ShardDownloader().populate_input_queue

[Show source in downloader.py:278](../../streaming_wds/core/downloader.py#L278)

Populate the download queue with shards assigned to the worker.

This method assigns shards to the worker based on the rank and worker information.
It can also shuffle the shards if specified.

#### Arguments

- `rank` *int* - The rank of the worker.
- `worker_infos` *WorkerInfoList* - List of worker information.
- `epoch` *int, optional* - The current epoch for shuffling. Defaults to 0.
- `shuffle` *bool, optional* - Whether to shuffle the shards. Defaults to False.

#### Signature

```python
def populate_input_queue(
    self, rank, worker_infos: WorkerInfoList, epoch: int = 0, shuffle: bool = False
): ...
```

### ShardDownloader().run

[Show source in downloader.py:342](../../streaming_wds/core/downloader.py#L342)

Run the download process with multiple worker threads.

This method starts multiple worker threads to download shards concurrently.
It waits for all worker threads to complete before setting the finish event.

#### Arguments

- `num_threads` *int* - The number of worker threads to start.
- `worker_info` *WorkerInfo* - Information about the worker.

#### Signature

```python
def run(
    self, num_threads: int, rank, worker_infos: WorkerInfoList, epoch: int, shuffle: bool
) -> None: ...
```

### ShardDownloader().run_worker

[Show source in downloader.py:305](../../streaming_wds/core/downloader.py#L305)

Run the worker to download shards.

This method continuously processes shards from the input queue until the stop event is set
or there are no more shards to process. It downloads each shard and puts them into the output queue.

#### Arguments

- `worker_info` *WorkerInfo* - Information about the worker.

#### Signature

```python
def run_worker(self, worker_info: WorkerInfo) -> None: ...
```

### ShardDownloader().set_queues

[Show source in downloader.py:157](../../streaming_wds/core/downloader.py#L157)

Set the input and output queues for the downloader.

#### Arguments

- `input_queue` *Queue* - Queue for incoming shard extraction requests.
- `output_queue` *Queue* - Queue for outputting extracted samples.

#### Signature

```python
def set_queues(self, input_queue: Queue, output_queue: Queue): ...
```



## count_shards

[Show source in downloader.py:76](../../streaming_wds/core/downloader.py#L76)

Helper function to count the number of shards in a dataset outside of the ShardDownloader.

#### Returns

- `int` - The number of shards.

#### Signature

```python
def count_shards(remote: str, session: Session) -> int: ...
```



## iterate_tarfiles

[Show source in downloader.py:27](../../streaming_wds/core/downloader.py#L27)

Helper function to iterate over all .tar files in a bucket, including compressed variants.

#### Arguments

- `bucket` *str* - The S3 bucket name.
- `key_prefix` *str* - The prefix for S3 keys.
- `session` *Session* - The boto3 session.

#### Returns

- `Iterator[str]` - An iterator over the keys.

#### Signature

```python
def iterate_tarfiles(bucket, key_prefix, s3_client): ...
```



## load_index

[Show source in downloader.py:49](../../streaming_wds/core/downloader.py#L49)

Load the dataset index from an S3 bucket.

This function attempts to retrieve and decode the dataset index file
from the specified S3 bucket and key prefix. The index file is expected
to be named 'index.wds'.

#### Arguments

- `bucket` *str* - The name of the S3 bucket.
- `key_prefix` *str* - The prefix for the S3 keys.
- `s3_client` *boto3.client* - The S3 client used to interact with the S3 service.

#### Returns

- `DatasetIndex` - The decoded dataset index.
If the index file does not exist, returns None.

#### Signature

```python
def load_index(bucket, key_prefix, s3_client) -> DatasetIndex: ...
```
