# Dataloader

[Streaming-wds Index](./README.md#streaming-wds-index) / Dataloader

> Auto-generated documentation for [dataloader](../streaming_wds/dataloader.py) module.

- [Dataloader](#dataloader)
  - [StreamingDataLoader](#streamingdataloader)
    - [StreamingDataLoader().gather_max_shard_idx_for_global_workers](#streamingdataloader()gather_max_shard_idx_for_global_workers)
    - [StreamingDataLoader().load_state_dict](#streamingdataloader()load_state_dict)
    - [StreamingDataLoader().prepare](#streamingdataloader()prepare)
    - [StreamingDataLoader().state_dict](#streamingdataloader()state_dict)
    - [StreamingDataLoader().update_local_max_shard_idx](#streamingdataloader()update_local_max_shard_idx)
  - [patch_collate_fn](#patch_collate_fn)

## StreamingDataLoader

[Show source in dataloader.py:101](../streaming_wds/dataloader.py#L101)

#### Signature

```python
class StreamingDataLoader(DataLoader):
    def __init__(
        self,
        dataset: StreamingWebDataset,
        num_workers: int = 0,
        shuffle: Optional[bool] = None,
        collate_fn: Optional[Callable] = None,
        *args: Any,
        **kwargs: Any
    ) -> None: ...
```

#### See also

- [StreamingWebDataset](./dataset.md#streamingwebdataset)

### StreamingDataLoader().gather_max_shard_idx_for_global_workers

[Show source in dataloader.py:230](../streaming_wds/dataloader.py#L230)

#### Signature

```python
def gather_max_shard_idx_for_global_workers(self) -> dict: ...
```

### StreamingDataLoader().load_state_dict

[Show source in dataloader.py:270](../streaming_wds/dataloader.py#L270)

#### Signature

```python
def load_state_dict(self, obj: Dict[str, Any]) -> None: ...
```

### StreamingDataLoader().prepare

[Show source in dataloader.py:153](../streaming_wds/dataloader.py#L153)

#### Signature

```python
def prepare(self, worker_infos: WorkerInfoList, resume: bool = False) -> None: ...
```

#### See also

- [WorkerInfoList](core/types.md#workerinfolist)

### StreamingDataLoader().state_dict

[Show source in dataloader.py:254](../streaming_wds/dataloader.py#L254)

#### Signature

```python
def state_dict(self) -> Dict[str, Any]: ...
```

### StreamingDataLoader().update_local_max_shard_idx

[Show source in dataloader.py:174](../streaming_wds/dataloader.py#L174)

Update the maximum shard index for local workers.

This method updates the maximum shard index for each local worker based on the
provided source ranks and shard indices. It ensures that the maximum shard index
for each worker is correctly tracked.

#### Arguments

- `source_ranks` *List[int]* - A list of source ranks corresponding to the workers.
- `shard_indices` *List[int]* - A list of shard indices corresponding to the shards
                           processed by the workers.

#### Signature

```python
def update_local_max_shard_idx(
    self, source_ranks: List[int], shard_indices: List[int]
): ...
```



## patch_collate_fn

[Show source in dataloader.py:17](../streaming_wds/dataloader.py#L17)

Patch a collate function to exclude certain WebDataset-specific keys from collation.

This function takes a collate function and returns a new function that wraps the original.
The new function removes specific keys (__wds_global_rank__, __wds_shard_idx__, and
__wds_sample_key__) from the input dictionaries before collation, then adds them back
to the collated output. It also checks that each item in the batch is a dictionary.

#### Arguments

- `collate_fn` *Callable* - The original collate function to be patched. This function
                       should take a list of dictionaries and return a single
                       dictionary with collated values.

#### Returns

- `Callable` - A new collate function that wraps the original, excluding specific keys
          from collation and re-adding them to the output.

#### Raises

- `TypeError` - If any item in the input batch is not a dictionary.

#### Examples

```python
>>> def original_collate(batch):
...     return {k: [d[k] for d in batch] for k in batch[0]}
>>> patched_collate = patch_collate_fn(original_collate)
>>> batch = [
...     {"data": 1, "__wds_global_rank__": 0},
...     {"data": 2, "__wds_global_rank__": 1}
... ]
>>> result = patched_collate(batch)
>>> print(result)
{'data': [1, 2], '__wds_global_rank__': [0, 1]}
```

#### Signature

```python
def patch_collate_fn(collate_fn: Callable) -> Callable: ...
```
