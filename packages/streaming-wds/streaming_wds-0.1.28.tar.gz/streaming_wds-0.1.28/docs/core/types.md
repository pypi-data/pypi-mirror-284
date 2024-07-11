# Types

[Streaming-wds Index](../README.md#streaming-wds-index) / [Core](./index.md#core) / Types

> Auto-generated documentation for [core.types](../../streaming_wds/core/types.py) module.

- [Types](#types)
  - [Bytes](#bytes)
  - [StateDict](#statedict)
    - [StateDict.from_dict](#statedictfrom_dict)
    - [StateDict().to_dict](#statedict()to_dict)
  - [WorkerInfo](#workerinfo)
    - [WorkerInfo.default](#workerinfodefault)
    - [WorkerInfo.from_dict](#workerinfofrom_dict)
    - [WorkerInfo().local_idx](#workerinfo()local_idx)
    - [WorkerInfo().to_dict](#workerinfo()to_dict)
  - [WorkerInfoList](#workerinfolist)
    - [WorkerInfoList.default](#workerinfolistdefault)
    - [WorkerInfoList.from_dict](#workerinfolistfrom_dict)
    - [WorkerInfoList().get_local](#workerinfolist()get_local)
    - [WorkerInfoList().to_dict](#workerinfolist()to_dict)

## Bytes

[Show source in types.py:121](../../streaming_wds/core/types.py#L121)

#### Signature

```python
class Bytes:
    def __init__(self, value: Union[int, str, "Bytes"]): ...
```



## StateDict

[Show source in types.py:99](../../streaming_wds/core/types.py#L99)

#### Signature

```python
class StateDict: ...
```

### StateDict.from_dict

[Show source in types.py:111](../../streaming_wds/core/types.py#L111)

#### Signature

```python
@classmethod
def from_dict(cls, d: Dict[str, Any]): ...
```

### StateDict().to_dict

[Show source in types.py:104](../../streaming_wds/core/types.py#L104)

#### Signature

```python
def to_dict(self) -> Dict[str, Any]: ...
```



## WorkerInfo

[Show source in types.py:9](../../streaming_wds/core/types.py#L9)

#### Signature

```python
class WorkerInfo: ...
```

### WorkerInfo.default

[Show source in types.py:17](../../streaming_wds/core/types.py#L17)

#### Signature

```python
@staticmethod
def default(dataset_len: int): ...
```

### WorkerInfo.from_dict

[Show source in types.py:39](../../streaming_wds/core/types.py#L39)

#### Signature

```python
@classmethod
def from_dict(cls, d: Dict[str, Any]): ...
```

### WorkerInfo().local_idx

[Show source in types.py:26](../../streaming_wds/core/types.py#L26)

#### Signature

```python
@property
def local_idx(self) -> int: ...
```

### WorkerInfo().to_dict

[Show source in types.py:30](../../streaming_wds/core/types.py#L30)

#### Signature

```python
def to_dict(self): ...
```



## WorkerInfoList

[Show source in types.py:51](../../streaming_wds/core/types.py#L51)

#### Signature

```python
class WorkerInfoList: ...
```

### WorkerInfoList.default

[Show source in types.py:63](../../streaming_wds/core/types.py#L63)

#### Signature

```python
@classmethod
def default(cls, dataset_len: int): ...
```

### WorkerInfoList.from_dict

[Show source in types.py:93](../../streaming_wds/core/types.py#L93)

#### Signature

```python
@classmethod
def from_dict(cls, d: Dict[str, Any]): ...
```

### WorkerInfoList().get_local

[Show source in types.py:76](../../streaming_wds/core/types.py#L76)

#### Signature

```python
def get_local(self, num_workers: int) -> "WorkerInfoList": ...
```

### WorkerInfoList().to_dict

[Show source in types.py:90](../../streaming_wds/core/types.py#L90)

#### Signature

```python
def to_dict(self) -> Dict[str, Any]: ...
```
