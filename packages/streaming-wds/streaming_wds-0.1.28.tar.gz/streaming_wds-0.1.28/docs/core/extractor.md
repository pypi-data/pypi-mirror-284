# Extractor

[Streaming-wds Index](../README.md#streaming-wds-index) / [Core](./index.md#core) / Extractor

> Auto-generated documentation for [core.extractor](../../streaming_wds/core/extractor.py) module.

- [Extractor](#extractor)
  - [ShardExtractor](#shardextractor)
    - [ShardExtractor().extract_shard](#shardextractor()extract_shard)
    - [ShardExtractor().run](#shardextractor()run)
    - [ShardExtractor().run_worker](#shardextractor()run_worker)
    - [ShardExtractor().set_queues](#shardextractor()set_queues)
    - [ShardExtractor().tar_member_iterator](#shardextractor()tar_member_iterator)
    - [ShardExtractor().tar_sample_iterator](#shardextractor()tar_sample_iterator)

## ShardExtractor

[Show source in extractor.py:17](../../streaming_wds/core/extractor.py#L17)

A class for extracting shards and processing their contents.

This class handles the extraction of shards from a local cache, processes their
contents, and puts the extracted samples into an output queue.

#### Attributes

- `input_queue` *Queue* - Queue for incoming shard extraction requests.
- `output_queue` *Queue* - Queue for outputting extracted samples.
- `stop_event` *threading.Event* - Event to signal stopping of the extraction process.
- `buffer_size` *int* - Maximum buffer size for memory management.
- `cache` *LocalShardLRUCache* - Local cache for storing and retrieving shards.
- `input_finish_event` *threading.Event* - Event to signal completion of input.
- `output_finish_event` *threading.Event* - Event to signal completion of output.

#### Signature

```python
class ShardExtractor:
    def __init__(
        self,
        input_queue: Queue,
        output_queue: Queue,
        stop_event: threading.Event,
        input_finish_event: threading.Event,
        output_finish_event: threading.Event,
        cache: LocalShardLRUCache,
        memory_buffer_limit_bytes: int,
        mode: Literal["r:*", "r|*"] = "r|*",
    ): ...
```

### ShardExtractor().extract_shard

[Show source in extractor.py:166](../../streaming_wds/core/extractor.py#L166)

Extract and process a single shard.

This method extracts the contents of a shard, processes its files, and yields
the aggregated data for each sample in the shard.

#### Arguments

- `shard_idx` *int* - The index of the shard.
- `shard_key` *str* - The key of the shard in the cache.
- `rank` *int* - The rank of the worker processing this shard.

#### Yields

- `dict` - A dictionary containing the aggregated data for each sample in the shard.

#### Raises

- `Exception` - If the shard is not found in the cache.

#### Signature

```python
def extract_shard(self, shard_idx: int, shard_key: str, rank: int): ...
```

### ShardExtractor().run

[Show source in extractor.py:244](../../streaming_wds/core/extractor.py#L244)

Run the extraction process with multiple worker threads.

This method starts multiple worker threads to process and extract shards concurrently.
It waits for all worker threads to complete before setting the output finish event.

#### Arguments

- `num_threads` *int* - The number of worker threads to start.
- `rank` *int* - The rank of the worker.

#### Signature

```python
def run(self, num_threads: int, rank: int) -> None: ...
```

### ShardExtractor().run_worker

[Show source in extractor.py:214](../../streaming_wds/core/extractor.py#L214)

Run the worker to process and extract shards.

This method continuously processes shards from the input queue until the stop event is set
or there are no more shards to process. It extracts samples from each shard and puts them
into the output queue.

#### Arguments

- `rank` *int* - The rank of the worker.

#### Signature

```python
def run_worker(self, rank: int): ...
```

### ShardExtractor().set_queues

[Show source in extractor.py:75](../../streaming_wds/core/extractor.py#L75)

Set the input and output queues for the extractor.

#### Arguments

- `input_queue` *Queue* - Queue for incoming shard extraction requests.
- `output_queue` *Queue* - Queue for outputting extracted samples.

#### Signature

```python
def set_queues(self, input_queue: Queue, output_queue: Queue): ...
```

### ShardExtractor().tar_member_iterator

[Show source in extractor.py:86](../../streaming_wds/core/extractor.py#L86)

Iterate over the members in a tar file based on the specified mode.

#### Arguments

- `tar` *tarfile.TarFile* - The tar file object to iterate over.

#### Yields

- `tarfile.TarInfo` - The next member in the tar file.

#### Raises

- `ValueError` - If the mode is not 'r:*' or 'r|*'.

#### Signature

```python
def tar_member_iterator(self, tar: tarfile.TarFile) -> List[tarfile.TarInfo]: ...
```

### ShardExtractor().tar_sample_iterator

[Show source in extractor.py:106](../../streaming_wds/core/extractor.py#L106)

Iterate over the members in a tar file and yield aggregated data for each sample.

This method reads the contents of a tar file, processes its files, and yields
the aggregated data for each sample in the tar file. The aggregation is based
on the sample key derived from the file names.

#### Arguments

- `fileobj` *BufferedReader* - The tar file object to read from.
- `shard_idx` *int* - The index of the shard.
- `rank` *int* - The rank of the worker processing this shard.

#### Yields

- `dict` - A dictionary containing the aggregated data for each sample in the tar file.

#### Signature

```python
def tar_sample_iterator(
    self, fileobj: BufferedReader, shard_idx: int, rank: int
) -> Generator[Dict[str, Union[pa.Buffer, int]], None, None]: ...
```
