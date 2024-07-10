# Utils

[Streaming-wds Index](./README.md#streaming-wds-index) / Utils

> Auto-generated documentation for [utils](../streaming_wds/utils.py) module.

- [Utils](#utils)
  - [cache_lock](#cache_lock)
  - [clear_stale_caches](#clear_stale_caches)
  - [empty_queue](#empty_queue)
  - [get_dist_rank](#get_dist_rank)
  - [get_dist_world_size](#get_dist_world_size)
  - [get_global_rank](#get_global_rank)
  - [get_global_world_size](#get_global_world_size)
  - [get_mp_rank](#get_mp_rank)
  - [get_mp_world_size](#get_mp_world_size)
  - [isolate_rng](#isolate_rng)

## cache_lock

[Show source in utils.py:165](../streaming_wds/utils.py#L165)

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



## clear_stale_caches

[Show source in utils.py:219](../streaming_wds/utils.py#L219)

Clear stale caches for a specific remote and split.

This function deletes the cache directory for the given remote and split.

#### Arguments

- `remote` *str* - The remote URL of the dataset.
- `split` *str* - The split name of the dataset.

#### Returns

- `bool` - True if the cache was successfully cleared, False otherwise.

#### Signature

```python
def clear_stale_caches(remote: str, split: Optional[str] = None): ...
```



## empty_queue

[Show source in utils.py:150](../streaming_wds/utils.py#L150)

Empty a queue by removing and discarding all its items.

#### Arguments

- `queue` *Queue* - The queue to be emptied.

#### Signature

```python
def empty_queue(queue: Queue): ...
```



## get_dist_rank

[Show source in utils.py:107](../streaming_wds/utils.py#L107)

Get the rank of the current process in the distributed training setup.

#### Returns

- `int` - The rank of the current process if distributed training is initialized,
     otherwise 0.

#### Signature

```python
def get_dist_rank() -> int: ...
```



## get_dist_world_size

[Show source in utils.py:79](../streaming_wds/utils.py#L79)

Get the number of processes in the distributed training setup.

#### Returns

- `int` - The number of distributed processes if distributed training is initialized,
     otherwise 1.

#### Signature

```python
def get_dist_world_size() -> int: ...
```



## get_global_rank

[Show source in utils.py:135](../streaming_wds/utils.py#L135)

Get the global rank of the current process, considering both distributed training
and DataLoader workers.

#### Returns

- `int` - The global rank of the current process.

#### Signature

```python
def get_global_rank() -> int: ...
```



## get_global_world_size

[Show source in utils.py:61](../streaming_wds/utils.py#L61)

Get the total number of workers across all distributed processes and data loader workers.

#### Returns

- `int` - The global world size, which is the product of the distributed world size
     and the number of data loader workers.

#### Signature

```python
def get_global_world_size() -> int: ...
```



## get_mp_rank

[Show source in utils.py:120](../streaming_wds/utils.py#L120)

Get the rank of the current DataLoader worker process.

#### Returns

- `int` - The rank of the current DataLoader worker if running in a worker process,
     otherwise 0.

#### Signature

```python
def get_mp_rank() -> int: ...
```



## get_mp_world_size

[Show source in utils.py:92](../streaming_wds/utils.py#L92)

Get the number of worker processes for the current DataLoader.

#### Returns

- `int` - The number of worker processes if running in a DataLoader worker,
     otherwise 1.

#### Signature

```python
def get_mp_world_size() -> int: ...
```



## isolate_rng

[Show source in utils.py:20](../streaming_wds/utils.py#L20)

A context manager that resets the global random state on exit to what it was before entering.

It supports isolating the states for PyTorch, Numpy, and Python built-in random number generators.

#### Arguments

- `include_cuda` - Whether to allow this function to also control the `torch.cuda` random number generator.
    Set this to ``False`` when using the function in a forked process where CUDA re-initialization is
    prohibited.

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
def isolate_rng(include_cuda: bool = True) -> Generator[None, None, None]: ...
```
