# Cache

[Streaming-wds Index](../README.md#streaming-wds-index) / [Core](./index.md#core) / Cache

> Auto-generated documentation for [core.cache](../../streaming_wds/core/cache.py) module.

- [Cache](#cache)
  - [LocalShardLRUCache](#localshardlrucache)
    - [LocalShardLRUCache()._evict_oldest_shard](#localshardlrucache()_evict_oldest_shard)
    - [LocalShardLRUCache().add_shard](#localshardlrucache()add_shard)
    - [LocalShardLRUCache().clear_partial_cache](#localshardlrucache()clear_partial_cache)
    - [LocalShardLRUCache().create_lock_file](#localshardlrucache()create_lock_file)
    - [LocalShardLRUCache().free_lock_file](#localshardlrucache()free_lock_file)
    - [LocalShardLRUCache().get_shard](#localshardlrucache()get_shard)
    - [LocalShardLRUCache().get_shard_path](#localshardlrucache()get_shard_path)
    - [LocalShardLRUCache().load_cache](#localshardlrucache()load_cache)
    - [LocalShardLRUCache().remove_shard](#localshardlrucache()remove_shard)
    - [LocalShardLRUCache().with_cache_lock](#localshardlrucache()with_cache_lock)
    - [LocalShardLRUCache().with_shard_lock](#localshardlrucache()with_shard_lock)

## LocalShardLRUCache

[Show source in cache.py:16](../../streaming_wds/core/cache.py#L16)

A local cache for shards using a Least Recently Used (LRU) eviction policy.

This class manages a local cache of shards, handling their storage, retrieval,
and eviction based on a size limit and access patterns.

#### Attributes

- `remote` *str* - The remote uri of the dataset.
- `bucket` *str* - The bucket name extracted from the remote uri.
- `key_prefix` *str* - The key prefix extracted from the remote uri.
- `cache_dir` *Path* - The local directory where shards are cached.
- `cache_limit_bytes` *int* - The maximum size of the cache in bytes.
- `current_cache_size` *int* - The current size of the cache in bytes.
- `cache_lock` *threading.Lock* - A lock for thread-safe cache operations.
shard_locks (Dict[str, threading.Lock]): Locks for individual shards.
shard_access_times (Dict[str, int]): Last access times for shards.
shard_read_count (Dict[str, int]): Read counts for shards.

#### Signature

```python
class LocalShardLRUCache:
    def __init__(
        self,
        remote: str,
        worker_rank: int,
        cache_limit_bytes: int,
        stop_event: threading.Event,
        overwrite: bool = False,
    ): ...
```

### LocalShardLRUCache()._evict_oldest_shard

[Show source in cache.py:322](../../streaming_wds/core/cache.py#L322)

Evict the oldest shard from the cache.

This method removes the least recently used shard that has been read more than once.
If no such shard exists, it waits and tries again.

#### Signature

```python
def _evict_oldest_shard(self) -> None: ...
```

### LocalShardLRUCache().add_shard

[Show source in cache.py:272](../../streaming_wds/core/cache.py#L272)

Add a new shard to the cache.

If there's not enough space, this method will evict old shards until there's room.

#### Arguments

- `shard_key` *str* - The key of the shard to add.
- `shard_size` *int* - The size of the shard in bytes.

#### Returns

- `str` - The path where the shard should be stored.

#### Signature

```python
def add_shard(self, shard_key: str, shard_size: int): ...
```

### LocalShardLRUCache().clear_partial_cache

[Show source in cache.py:83](../../streaming_wds/core/cache.py#L83)

Clear any partially downloaded files in the cache, including those in subdirectories.

#### Signature

```python
def clear_partial_cache(self): ...
```

### LocalShardLRUCache().create_lock_file

[Show source in cache.py:132](../../streaming_wds/core/cache.py#L132)

Create a lock file to prevent other processes from modifying the cache.
If the lock file already exists, raise an exception.

#### Signature

```python
def create_lock_file(self): ...
```

### LocalShardLRUCache().free_lock_file

[Show source in cache.py:146](../../streaming_wds/core/cache.py#L146)

Remove the lock file to allow other processes to modify the cache.

#### Signature

```python
def free_lock_file(self): ...
```

### LocalShardLRUCache().get_shard

[Show source in cache.py:190](../../streaming_wds/core/cache.py#L190)

Get a shard from the cache.

This method updates the access time and read count for the shard.

#### Arguments

- `shard_key` *str* - The key of the shard to retrieve.

#### Returns

- `Optional[str]` - The path to the shard if it exists in the cache, None otherwise.

#### Signature

```python
def get_shard(self, shard_key: str) -> Optional[str]: ...
```

### LocalShardLRUCache().get_shard_path

[Show source in cache.py:173](../../streaming_wds/core/cache.py#L173)

Get the local path for a shard.

#### Arguments

- `shard_key` *str* - The key of the shard.
- `check_exists` *bool* - If True, return None if the shard doesn't exist.

#### Returns

- `str` - The local path of the shard, or None if check_exists is True and the shard doesn't exist.

#### Signature

```python
def get_shard_path(self, shard_key: str, check_exists: bool = False) -> str: ...
```

### LocalShardLRUCache().load_cache

[Show source in cache.py:153](../../streaming_wds/core/cache.py#L153)

Load the cache, clearing existing content if present.

This method ensures the cache directory exists and is empty.

#### Signature

```python
def load_cache(self) -> None: ...
```

### LocalShardLRUCache().remove_shard

[Show source in cache.py:296](../../streaming_wds/core/cache.py#L296)

Remove a shard from the cache.

#### Arguments

- `shard_key` *str* - The key of the shard to remove.

#### Signature

```python
def remove_shard(self, shard_key: str): ...
```

### LocalShardLRUCache().with_cache_lock

[Show source in cache.py:221](../../streaming_wds/core/cache.py#L221)

Acquire the cache lock for the duration of a context manager.

#### Yields

- `bool` - True if the lock was acquired, False if the lock is already held.

#### Signature

```python
@contextmanager
def with_cache_lock(self): ...
```

### LocalShardLRUCache().with_shard_lock

[Show source in cache.py:239](../../streaming_wds/core/cache.py#L239)

Acquire the lock for a specific shard for the duration of a context manager.

#### Arguments

- `shard_key` *str* - The key of the shard to lock.

#### Yields

- `bool` - True if the lock was acquired, False if the shard doesn't exist.

#### Signature

```python
@contextmanager
def with_shard_lock(self, shard_key: str): ...
```
