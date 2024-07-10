# Dataset

[Streaming-wds Index](./README.md#streaming-wds-index) / Dataset

> Auto-generated documentation for [dataset](../streaming_wds/dataset.py) module.

- [Dataset](#dataset)
  - [StreamingWebDataset](#streamingwebdataset)
    - [StreamingWebDataset().__del__](#streamingwebdataset()__del__)
    - [StreamingWebDataset().__iter__](#streamingwebdataset()__iter__)
    - [StreamingWebDataset()._decode_sample](#streamingwebdataset()_decode_sample)
    - [StreamingWebDataset().clear_worker_components](#streamingwebdataset()clear_worker_components)
    - [StreamingWebDataset().global_rank](#streamingwebdataset()global_rank)
    - [StreamingWebDataset().num_shards](#streamingwebdataset()num_shards)
    - [StreamingWebDataset().prepare_worker_components](#streamingwebdataset()prepare_worker_components)
    - [StreamingWebDataset().process_sample](#streamingwebdataset()process_sample)
    - [StreamingWebDataset().reset_global_rank](#streamingwebdataset()reset_global_rank)
    - [StreamingWebDataset().set_epoch](#streamingwebdataset()set_epoch)
    - [StreamingWebDataset().set_shuffle](#streamingwebdataset()set_shuffle)
    - [StreamingWebDataset().set_worker_infos](#streamingwebdataset()set_worker_infos)

## StreamingWebDataset

[Show source in dataset.py:25](../streaming_wds/dataset.py#L25)

#### Signature

```python
class StreamingWebDataset(IterableDataset):
    def __init__(
        self,
        remote: str,
        split: Optional[str] = None,
        profile: str = "default",
        shuffle: bool = False,
        max_workers: int = 2,
        schema: Dict[str, str] = {},
        memory_buffer_limit_bytes: Union[Bytes, int, str] = "2GB",
        file_cache_limit_bytes: Union[Bytes, int, str] = "2GB",
    ): ...
```

#### See also

- [Bytes](core/types.md#bytes)

### StreamingWebDataset().__del__

[Show source in dataset.py:349](../streaming_wds/dataset.py#L349)

Clean up resources when the dataset object is deleted.

This method stops all worker threads and deletes the cache.

#### Signature

```python
def __del__(self): ...
```

### StreamingWebDataset().__iter__

[Show source in dataset.py:258](../streaming_wds/dataset.py#L258)

Create an iterator for the dataset.

This method initializes the worker components, starts the worker threads,
and yields processed samples from the dataset.

#### Yields

- `Dict[str,` *Any]* - Processed and decoded samples from the dataset.

#### Raises

- `ValueError` - If an internal key is reintroduced in the process_sample method.
- `Exception` - If an error occurs during iteration.

#### Signature

```python
def __iter__(self): ...
```

### StreamingWebDataset()._decode_sample

[Show source in dataset.py:224](../streaming_wds/dataset.py#L224)

Decode a sample using the specified decoders.

#### Arguments

sample (Dict[str, bytes]): The sample to decode.

#### Returns

- `Dict[str,` *Any]* - The decoded sample.

#### Signature

```python
def _decode_sample(self, sample: Dict[str, bytes]) -> Dict[str, Any]: ...
```

### StreamingWebDataset().clear_worker_components

[Show source in dataset.py:98](../streaming_wds/dataset.py#L98)

Clear the worker components of the dataset.

This method clears the worker components and sets the worker components initialized flag to False.

#### Signature

```python
def clear_worker_components(self): ...
```

### StreamingWebDataset().global_rank

[Show source in dataset.py:206](../streaming_wds/dataset.py#L206)

Get the global rank of the current worker.

#### Returns

- `int` - The global rank of the current worker.

#### Signature

```python
@property
def global_rank(self): ...
```

### StreamingWebDataset().num_shards

[Show source in dataset.py:70](../streaming_wds/dataset.py#L70)

Get the total number of shards in the dataset.

#### Returns

- `int` - The number of shards in the dataset.

#### Signature

```python
@property
def num_shards(self): ...
```

### StreamingWebDataset().prepare_worker_components

[Show source in dataset.py:120](../streaming_wds/dataset.py#L120)

Reset the worker components of the dataset.

This method resets the global rank and reinitializes the worker components if they haven't been initialized before.
If the components were already initialized, it empties the queues and resets the events.

#### Signature

```python
def prepare_worker_components(self): ...
```

### StreamingWebDataset().process_sample

[Show source in dataset.py:244](../streaming_wds/dataset.py#L244)

Process a sample before decoding.

This method can be overridden to implement custom processing logic.

#### Arguments

sample (Dict[str, bytes]): The sample to process.

#### Returns

- `Dict[str,` *bytes]* - The processed sample.

#### Signature

```python
def process_sample(self, sample: Dict[str, bytes]) -> Dict[str, bytes]: ...
```

### StreamingWebDataset().reset_global_rank

[Show source in dataset.py:218](../streaming_wds/dataset.py#L218)

Reset the cached global rank of the current worker.

#### Signature

```python
def reset_global_rank(self): ...
```

### StreamingWebDataset().set_epoch

[Show source in dataset.py:80](../streaming_wds/dataset.py#L80)

Set the epoch for the dataset.

#### Arguments

- `epoch` *int* - The epoch to set.

#### Signature

```python
def set_epoch(self, epoch: int): ...
```

### StreamingWebDataset().set_shuffle

[Show source in dataset.py:197](../streaming_wds/dataset.py#L197)

Set the shuffle parameter for the dataset.

#### Arguments

- `shuffle` *bool* - Whether to shuffle the data or not.

#### Signature

```python
def set_shuffle(self, shuffle: bool): ...
```

### StreamingWebDataset().set_worker_infos

[Show source in dataset.py:89](../streaming_wds/dataset.py#L89)

Set the worker information for the dataset.

#### Arguments

- `worker_infos` *List[WorkerInfo]* - A list of WorkerInfo objects containing information about each worker.

#### Signature

```python
def set_worker_infos(self, worker_infos: List[WorkerInfo]): ...
```

#### See also

- [WorkerInfo](core/types.md#workerinfo)
