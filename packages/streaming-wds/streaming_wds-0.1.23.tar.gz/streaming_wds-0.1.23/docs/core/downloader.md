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
    - [ShardDownloader().prefetch_shards](#sharddownloader()prefetch_shards)
    - [ShardDownloader().run](#sharddownloader()run)
    - [ShardDownloader().set_queues](#sharddownloader()set_queues)
  - [count_shards](#count_shards)

## DownloadCancelled

[Show source in downloader.py:20](../../streaming_wds/core/downloader.py#L20)

#### Signature

```python
class DownloadCancelled(Exception): ...
```



## ShardDownloader

[Show source in downloader.py:47](../../streaming_wds/core/downloader.py#L47)

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

[Show source in downloader.py:167](../../streaming_wds/core/downloader.py#L167)

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

[Show source in downloader.py:154](../../streaming_wds/core/downloader.py#L154)

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

[Show source in downloader.py:138](../../streaming_wds/core/downloader.py#L138)

Find all shards in the S3 bucket with the given prefix.

#### Returns

- `List[str]` - A list of shard keys.

#### Signature

```python
def find_shards(self): ...
```

### ShardDownloader().get_shard

[Show source in downloader.py:198](../../streaming_wds/core/downloader.py#L198)

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

[Show source in downloader.py:123](../../streaming_wds/core/downloader.py#L123)

Get the number of shards.

#### Returns

- `int` - The number of shards.

#### Signature

```python
def num_shards(self): ...
```

### ShardDownloader().prefetch_shards

[Show source in downloader.py:231](../../streaming_wds/core/downloader.py#L231)

Prefetch multiple shards in parallel.

#### Arguments

- `keys` *List[str]* - List of S3 keys to prefetch.

#### Signature

```python
def prefetch_shards(self, keys: List[str]): ...
```

### ShardDownloader().run

[Show source in downloader.py:243](../../streaming_wds/core/downloader.py#L243)

Run the shard downloading process for a worker.

#### Arguments

- `worker_info` *WorkerInfo* - Information about the worker.

#### Raises

- `RuntimeError` - If setup() was not called before run().

#### Signature

```python
def run(
    self, rank, worker_infos: List[WorkerInfo], epoch: int = 0, shuffle: bool = False
): ...
```

### ShardDownloader().set_queues

[Show source in downloader.py:112](../../streaming_wds/core/downloader.py#L112)

Set the input and output queues for the downloader.

#### Arguments

- `input_queue` *Queue* - Queue for incoming shard extraction requests.
- `output_queue` *Queue* - Queue for outputting extracted samples.

#### Signature

```python
def set_queues(self, input_queue: Queue, output_queue: Queue): ...
```



## count_shards

[Show source in downloader.py:24](../../streaming_wds/core/downloader.py#L24)

Helper function to count the number of shards in a dataset outside of the ShardDownloader.

#### Returns

- `List[str]` - A list of shard keys.

#### Signature

```python
def count_shards(remote: str, session: Session) -> List[str]: ...
```
