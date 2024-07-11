import logging
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import torch.distributed as dist
from torch.utils.data import DataLoader

from .core.sharder import compute_worker_infos, distribute_worker_infos
from .core.types import StateDict, WorkerInfoList
from .dataset import StreamingWebDataset
from .utils import get_dist_world_size

logger = logging.getLogger(__name__)

# TODO: most of this logic should be refactored into custom dataloader iterators


def patch_collate_fn(collate_fn: Callable) -> Callable:
    """
    Patch a collate function to exclude certain WebDataset-specific keys from collation.

    This function takes a collate function and returns a new function that wraps the original.
    The new function removes specific keys (__wds_global_rank__, __wds_shard_idx__, and
    __wds_sample_key__) from the input dictionaries before collation, then adds them back
    to the collated output. It also checks that each item in the batch is a dictionary.

    Args:
        collate_fn (Callable): The original collate function to be patched. This function
                               should take a list of dictionaries and return a single
                               dictionary with collated values.

    Returns:
        Callable: A new collate function that wraps the original, excluding specific keys
                  from collation and re-adding them to the output.

    Raises:
        TypeError: If any item in the input batch is not a dictionary.

    Example:
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
    """

    def patched_collate(
        batch: Union[List[Dict[str, Any]], List[Tuple]],
    ) -> Union[Dict[str, List[Any]], Tuple[List[Any]]]:
        if all(isinstance(item, dict) for item in batch):
            # Keys to exclude from collation
            exclude_keys = [
                "__wds_global_rank__",
                "__wds_shard_idx__",
                "__wds_sample_key__",
            ]
            excluded_values = {key: [] for key in exclude_keys}

            # Remove excluded keys from each item in the batch
            filtered_batch = []
            for item in batch:
                filtered_item = {}
                for key, value in item.items():
                    if key in exclude_keys:
                        excluded_values[key].append(value)
                    else:
                        filtered_item[key] = value
                filtered_batch.append(filtered_item)

            # Call the original collate function on the filtered batch
            collated = collate_fn(filtered_batch)

            # Add back the excluded keys
            for key in exclude_keys:
                if excluded_values[key]:
                    collated[key] = excluded_values[key]

        elif all(isinstance(item, tuple) for item in batch):
            ranks = [item[-3] for item in batch]
            shard_indices = [item[-2] for item in batch]
            sample_keys = [item[-1] for item in batch]

            batch = [item[:-3] for item in batch]
            collated = collate_fn(batch)
            collated = (*collated, ranks, shard_indices, sample_keys)

        else:
            raise ValueError(
                "The input batch should contain either dictionaries or tuples."
            )

        return collated

    return patched_collate


class StreamingDataLoader(DataLoader):
    __doc__ = DataLoader.__doc__

    def __init__(
        self,
        dataset: StreamingWebDataset,
        *args: Any,
        num_workers: int = 0,
        shuffle: Optional[bool] = None,
        collate_fn: Optional[Callable] = None,
        **kwargs: Any,
    ) -> None:  # pyright: ignore
        if not isinstance(dataset, (StreamingWebDataset)):
            raise RuntimeError(
                "The provided dataset should be an instance of StreamingWebDataset."
                f" Found {dataset}."
            )

        self.current_epoch = -1
        self.resume = False

        self.num_shards = dataset.num_shards
        self.global_world_size = get_dist_world_size() * num_workers or 1

        # NOTE: if we run into issues where memory-usage grows unbounded due to fork
        # we can turn WorkerInfosList into a DictTensor instead of a dataclass
        self.worker_infos = compute_worker_infos(
            num_shards=self.num_shards, global_world_size=self.global_world_size
        )
        self.max_shard_idx_for_local_workers: Dict[int, int] = {
            worker_info.rank: 0
            for worker_info in self.worker_infos.get_local(num_workers)
        }
        self.rpc_group = None

        dataset.set_worker_infos(self.worker_infos)
        dataset.clear_worker_components()

        if shuffle is not None:
            dataset.set_shuffle(shuffle)

        if collate_fn is not None:
            collate_fn = patch_collate_fn(collate_fn)

        super().__init__(
            dataset,
            *args,
            num_workers=num_workers,
            collate_fn=collate_fn,
            **kwargs,
        )

    def prepare(self, worker_infos: WorkerInfoList, resume: bool = False) -> None:
        global_world_size = get_dist_world_size() * self.num_workers or 1
        logger.debug(
            f"Preparing StreamingDataLoader with global world size: {self.global_world_size}"
        )

        self.worker_infos = distribute_worker_infos(
            worker_infos,
            global_world_size=global_world_size,
            resume=resume,
        )

        self.dataset.set_worker_infos(self.worker_infos)
        self.dataset.set_epoch(self.current_epoch)

        # update local max shard idx
        self.max_shard_idx_for_local_workers = {
            worker_info.rank: worker_info.idx
            for worker_info in self.worker_infos.get_local(self.num_workers)
        }

    def update_local_max_shard_idx(
        self,
        source_ranks: List[int],
        shard_indices: List[int],
    ):
        """
        Update the maximum shard index for local workers.

        This method updates the maximum shard index for each local worker based on the
        provided source ranks and shard indices. It ensures that the maximum shard index
        for each worker is correctly tracked.

        Args:
            source_ranks (List[int]): A list of source ranks corresponding to the workers.
            shard_indices (List[int]): A list of shard indices corresponding to the shards
                                       processed by the workers.
        """
        for source_rank, shard_idx in zip(source_ranks, shard_indices):
            source_rank, shard_idx = int(source_rank), int(shard_idx)

            new_max_value = max(
                self.max_shard_idx_for_local_workers[source_rank], shard_idx
            )
            self.max_shard_idx_for_local_workers[source_rank] = new_max_value

    def __iter__(self) -> Any:
        if not self.resume:
            self.current_epoch += 1

        self.resume = True
        self.prepare(self.worker_infos, resume=self.resume)

        for batch in super().__iter__():
            # parse internal keys
            if isinstance(batch, dict):
                source_ranks = batch.pop("__wds_global_rank__")
                shard_indices = batch.pop("__wds_shard_idx__")
                _ = batch.pop("__wds_sample_key__")
            elif isinstance(batch, (tuple, list)):
                source_ranks, shard_indices, _ = batch[-3:]
                batch = batch[:-3]
            else:
                raise ValueError(
                    "The input batch should contain either dictionaries or tuples. "
                    f"Found {type(batch)}"
                )

            self.update_local_max_shard_idx(source_ranks, shard_indices)
            yield batch

        # Epoch ended
        self.resume = False
        self.max_shard_idx_for_local_workers = {
            k: 0 for k in self.max_shard_idx_for_local_workers
        }

    def gather_max_shard_idx_for_global_workers(self) -> dict:
        if not dist.is_initialized():
            return self.max_shard_idx_for_local_workers.copy()

        max_shard_idx_for_global_workers_list = [
            self.max_shard_idx_for_local_workers
        ] * dist.get_world_size()

        dist.all_gather_object(
            max_shard_idx_for_global_workers_list, self.max_shard_idx_for_local_workers
        )
        dist.broadcast_object_list(max_shard_idx_for_global_workers_list, src=0)

        # convert list to dict, all of them have unique keys
        max_shard_idx_for_global_workers = {}
        for (
            max_shard_idx_for_global_workers_dict
        ) in max_shard_idx_for_global_workers_list:
            max_shard_idx_for_global_workers.update(
                max_shard_idx_for_global_workers_dict
            )

        return max_shard_idx_for_global_workers

    def state_dict(self) -> Dict[str, Any]:
        max_shard_idx_for_global_workers = (
            self.gather_max_shard_idx_for_global_workers()
        )

        # update worker infos
        for worker_info in self.worker_infos:
            worker_info.idx = int(max_shard_idx_for_global_workers[worker_info.rank])
            worker_info.resume = self.resume

        return StateDict(
            epoch=max(0, self.current_epoch),
            num_shards=self.num_shards,
            worker_infos=self.worker_infos,
        ).to_dict()

    def load_state_dict(self, obj: Dict[str, Any]) -> None:
        state_dict = StateDict.from_dict(obj)

        self.current_epoch = state_dict.epoch
        self.worker_infos = state_dict.worker_infos
        self.resume = all(worker_info.resume for worker_info in self.worker_infos)

        if state_dict.num_shards != self.num_shards:
            raise RuntimeError(
                f"Number of shards in the state_dict ({state_dict.num_shards}) "
                f"does not match the number of shards in the dataset ({self.num_shards})."
            )
