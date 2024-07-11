# Index

[Streaming-wds Index](../README.md#streaming-wds-index) / [Core](#core) / Index

> Auto-generated documentation for [core.index](../../streaming_wds/core/index.py) module.

- [Index](#index)
  - [DatasetIndex](#datasetindex)
    - [DatasetIndex.decode](#datasetindexdecode)
    - [DatasetIndex().encode](#datasetindex()encode)
    - [DatasetIndex.from_dict](#datasetindexfrom_dict)
    - [DatasetIndex().shard_keys](#datasetindex()shard_keys)
    - [DatasetIndex().to_dict](#datasetindex()to_dict)
  - [ShardIndex](#shardindex)
    - [ShardIndex.from_dict](#shardindexfrom_dict)
    - [ShardIndex().to_dict](#shardindex()to_dict)

## DatasetIndex

[Show source in index.py:30](../../streaming_wds/core/index.py#L30)

#### Signature

```python
class DatasetIndex: ...
```

### DatasetIndex.decode

[Show source in index.py:57](../../streaming_wds/core/index.py#L57)

#### Signature

```python
@classmethod
def decode(cls, data: bytes): ...
```

### DatasetIndex().encode

[Show source in index.py:54](../../streaming_wds/core/index.py#L54)

#### Signature

```python
def encode(self): ...
```

### DatasetIndex.from_dict

[Show source in index.py:46](../../streaming_wds/core/index.py#L46)

#### Signature

```python
@classmethod
def from_dict(cls, data: dict): ...
```

### DatasetIndex().shard_keys

[Show source in index.py:35](../../streaming_wds/core/index.py#L35)

#### Signature

```python
@property
def shard_keys(self) -> str: ...
```

### DatasetIndex().to_dict

[Show source in index.py:39](../../streaming_wds/core/index.py#L39)

#### Signature

```python
def to_dict(self): ...
```



## ShardIndex

[Show source in index.py:11](../../streaming_wds/core/index.py#L11)

#### Signature

```python
class ShardIndex: ...
```

### ShardIndex.from_dict

[Show source in index.py:21](../../streaming_wds/core/index.py#L21)

#### Signature

```python
@classmethod
def from_dict(cls, data: dict): ...
```

### ShardIndex().to_dict

[Show source in index.py:15](../../streaming_wds/core/index.py#L15)

#### Signature

```python
def to_dict(self): ...
```
