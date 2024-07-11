# Utils

[Streaming-wds Index](./README.md#streaming-wds-index) / Utils

> Auto-generated documentation for [utils](../streaming_wds/utils.py) module.

- [Utils](#utils)
  - [cache_lock](#cache_lock)
  - [clean_stale_cache](#clean_stale_cache)
  - [compute_dataset_index](#compute_dataset_index)
  - [compute_shard_index](#compute_shard_index)
  - [empty_queue](#empty_queue)
  - [get_dist_rank](#get_dist_rank)
  - [get_dist_world_size](#get_dist_world_size)
  - [get_global_rank](#get_global_rank)
  - [get_global_world_size](#get_global_world_size)
  - [get_mp_rank](#get_mp_rank)
  - [get_mp_world_size](#get_mp_world_size)
  - [isolate_torch_rng](#isolate_torch_rng)
  - [parse_uri](#parse_uri)
  - [update_global_tensordict](#update_global_tensordict)

## cache_lock

[Show source in utils.py:191](../streaming_wds/utils.py#L191)

A context manager that uses a file lock to ensure the code within is executed only once.

This function creates a lock file based on the remote URL and split, and attempts to acquire
a lock on this file. If successful, it yields True, indicating that the calling process
should execute the code within the context. If unsuccessful, it yields False, indicating
that the calling process should skip the code within the context.

#### Arguments

- `remote` *str* - The remote URL of the dataset.
- `split` *Optional[str]* - The split name of the dataset, if applicable.

#### Yields

- `bool` - True if the lock was acquired (indicating the process should execute the code),
      False otherwise.

#### Examples

with cache_lock("https://example.com/data", "train") as acquired:
    if acquired:
        # This code will only be executed by one process
        download_and_process_data()

#### Signature

```python
@contextmanager
def cache_lock(remote: str, split: Optional[str] = None, rank: Optional[int] = None): ...
```



## clean_stale_cache

[Show source in utils.py:242](../streaming_wds/utils.py#L242)

Clear stale caches for a specific remote and split.

This function deletes the cache directory for the given remote and split.

#### Arguments

- `remote` *str* - The remote URL of the dataset.
- `split` *str* - The split name of the dataset.

#### Returns

- `bool` - True if the cache was successfully cleared, False otherwise.

#### Signature

```python
def clean_stale_cache(remote: str, split: Optional[str] = None): ...
```



## compute_dataset_index

[Show source in utils.py:315](../streaming_wds/utils.py#L315)

Compute the index for a dataset stored in S3.

This function calculates the index for a dataset by processing all shards
in the specified S3 location. It counts the number of shards and items,
and optionally writes the index back to S3.

#### Arguments

- `remote` *str* - The S3 URI of the dataset.
- `split` *Optional[str]* - The dataset split to process. If provided,
    it will be appended to the remote path.
- `profile` *Optional[str]* - The AWS profile name to use for authentication.
- `write` *bool* - If True, write the computed index back to S3.

#### Returns

- `DatasetIndex` - An object containing the computed index information.

#### Raises

- `ValueError` - If no shards are found in the specified location.

#### Signature

```python
def compute_dataset_index(
    remote: str,
    split: Optional[str] = None,
    profile: Optional[str] = None,
    write: bool = False,
): ...
```



## compute_shard_index

[Show source in utils.py:273](../streaming_wds/utils.py#L273)

Compute the index for a single shard in an S3 bucket.

This function retrieves a tar file from S3, reads its contents, and computes
the number of samples in the shard. It uses retry logic to handle potential
transient errors when interacting with S3.

#### Arguments

- `bucket` *str* - The name of the S3 bucket containing the shard.
- `shard_key` *str* - The key (path) of the shard file in the S3 bucket.
- `session` *Session* - An authenticated boto3 Session object for S3 access.

#### Returns

- `ShardIndex` - An object containing the shard key and the number of samples in the shard.

#### Raises

Any exceptions from S3 operations or file processing that persist after retries.

#### Signature

```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10),
    reraise=True,
)
def compute_shard_index(bucket: str, shard_key: str, session: Session) -> ShardIndex: ...
```

#### See also

- [ShardIndex](core/index.md#shardindex)



## empty_queue

[Show source in utils.py:160](../streaming_wds/utils.py#L160)

Empty a queue by removing and discarding all its items.

#### Arguments

- `queue` *Queue* - The queue to be emptied.

#### Signature

```python
def empty_queue(queue: Queue): ...
```



## get_dist_rank

[Show source in utils.py:95](../streaming_wds/utils.py#L95)

Get the rank of the current process in the distributed training setup.

#### Returns

- `int` - The rank of the current process if distributed training is initialized,
     otherwise 0.

#### Signature

```python
def get_dist_rank() -> int: ...
```



## get_dist_world_size

[Show source in utils.py:67](../streaming_wds/utils.py#L67)

Get the number of processes in the distributed training setup.

#### Returns

- `int` - The number of distributed processes if distributed training is initialized,
     otherwise 1.

#### Signature

```python
def get_dist_world_size() -> int: ...
```



## get_global_rank

[Show source in utils.py:123](../streaming_wds/utils.py#L123)

Get the global rank of the current process, considering both distributed training
and DataLoader workers.

#### Returns

- `int` - The global rank of the current process.

#### Signature

```python
def get_global_rank() -> int: ...
```



## get_global_world_size

[Show source in utils.py:49](../streaming_wds/utils.py#L49)

Get the total number of workers across all distributed processes and data loader workers.

#### Returns

- `int` - The global world size, which is the product of the distributed world size
     and the number of data loader workers.

#### Signature

```python
def get_global_world_size() -> int: ...
```



## get_mp_rank

[Show source in utils.py:108](../streaming_wds/utils.py#L108)

Get the rank of the current DataLoader worker process.

#### Returns

- `int` - The rank of the current DataLoader worker if running in a worker process,
     otherwise 0.

#### Signature

```python
def get_mp_rank() -> int: ...
```



## get_mp_world_size

[Show source in utils.py:80](../streaming_wds/utils.py#L80)

Get the number of worker processes for the current DataLoader.

#### Returns

- `int` - The number of worker processes if running in a DataLoader worker,
     otherwise 1.

#### Signature

```python
def get_mp_world_size() -> int: ...
```



## isolate_torch_rng

[Show source in utils.py:27](../streaming_wds/utils.py#L27)

A context manager that resets the torch global random state on exit to what it was before entering.

#### Examples

```python
>>> import torch
>>> torch.manual_seed(1)  # doctest: +ELLIPSIS
<torch._C.Generator object at ...>
>>> with isolate_rng():
...     [torch.rand(1) for _ in range(3)]
[tensor([0.7576]), tensor([0.2793]), tensor([0.4031])]
>>> torch.rand(1)
tensor([0.7576])
```

#### Signature

```python
@contextmanager
def isolate_torch_rng() -> Generator[None, None, None]: ...
```



## parse_uri

[Show source in utils.py:175](../streaming_wds/utils.py#L175)

Parse a URI into a bucket and key.

#### Arguments

- `uri` *str* - The URI to be parsed.

#### Returns

- `Tuple[str,` *str]* - A tuple containing the bucket and key parsed from the URI.

#### Signature

```python
def parse_uri(uri: str) -> Tuple[str, str]: ...
```



## update_global_tensordict

[Show source in utils.py:138](../streaming_wds/utils.py#L138)

Update the global TensorDict with values from the local TensorDict.

This function updates the global TensorDict with the values from the local TensorDict.
It's typically used in distributed settings to synchronize data across processes.

#### Arguments

- `global_dict` *TensorDict* - The global TensorDict to be updated.
- `local_dict` *TensorDict* - The local TensorDict containing the updates.

#### Returns

- `TensorDict` - The updated global TensorDict.

#### Notes

This function modifies the global_dict in-place and also returns it.

#### Signature

```python
def update_global_tensordict(
    global_dict: TensorDict, local_dict: TensorDict
) -> TensorDict: ...
```
