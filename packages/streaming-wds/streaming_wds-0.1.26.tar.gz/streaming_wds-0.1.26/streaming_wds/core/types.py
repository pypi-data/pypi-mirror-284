import re
from dataclasses import dataclass
from typing import Any, Dict, List, Union

from streaming_wds.utils import get_dist_rank, get_mp_world_size


@dataclass
class WorkerInfo:
    start: int  # global start index
    end: int  # global end index

    rank: int = 0  # global rank
    idx: int = 0  # max global idx
    resume: bool = False

    @staticmethod
    def default(dataset_len: int):
        return WorkerInfo(
            start=0,
            end=dataset_len - 1,
            rank=0,
            idx=0,
        )

    @property
    def local_idx(self) -> int:
        return self.idx - self.start

    def to_dict(self):
        return {
            "start": self.start,
            "end": self.end,
            "rank": self.rank,
            "idx": self.idx,
            "resume": self.resume,
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            start=d["start"],
            end=d["end"],
            rank=d["rank"],
            idx=d["idx"],
            resume=d["resume"],
        )


@dataclass
class WorkerInfoList:
    worker_infos: List[WorkerInfo]

    def __len__(self):
        return len(self.worker_infos)

    def __getitem__(self, index):
        return self.worker_infos[index]

    def __iter__(self):
        return iter(self.worker_infos)

    @classmethod
    def default(cls, dataset_len: int):
        return cls(
            worker_infos=[
                WorkerInfo(
                    start=0,
                    end=dataset_len - 1,
                    rank=0,
                    idx=0,
                ),
            ]
        )

    def get_local(self, num_workers: int) -> "WorkerInfoList":
        mp_world_size = num_workers or get_mp_world_size()
        dist_rank = get_dist_rank()

        # Calculate the global ranks for the multiprocessing workers on this distributed worker
        global_ranks = [
            dist_rank * mp_world_size + mp_rank for mp_rank in range(mp_world_size)
        ]

        # Filter the worker_infos to only include those for the current distributed worker
        return WorkerInfoList(
            worker_infos=[wi for wi in self.worker_infos if wi.rank in global_ranks]
        )

    def to_dict(self) -> Dict[str, Any]:
        return {"worker_infos": [w.to_dict() for w in self.worker_infos]}

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(worker_infos=[WorkerInfo.from_dict(w) for w in d["worker_infos"]])


@dataclass
class StateDict:
    epoch: int
    num_shards: int
    worker_infos: WorkerInfoList

    def to_dict(self) -> Dict[str, Any]:
        return {
            "epoch": self.epoch,
            "num_shards": self.num_shards,
            "worker_infos": self.worker_infos.to_dict(),
        }

    @classmethod
    def from_dict(cls, d: Dict[str, Any]):
        return cls(
            epoch=d["epoch"],
            num_shards=d["num_shards"],
            worker_infos=WorkerInfoList.from_dict(d["worker_infos"]),
        )


@dataclass
class Bytes:
    bytes: int

    def __init__(self, value: Union[int, str, "Bytes"]):
        if isinstance(value, int):
            self.bytes = value
        elif isinstance(value, str):
            self.bytes = self._parse_string(value)
        elif isinstance(value, Bytes):
            self.bytes = value.bytes
        else:
            raise ValueError("Input must be an integer, a string, or a Bytes object")

    def _parse_string(self, value: str) -> int:
        units: dict[str, int] = {
            "B": 1,
            "KB": 1024,
            "MB": 1024**2,
            "GB": 1024**3,
            "TB": 1024**4,
            "PB": 1024**5,
        }

        match = re.match(r"^(\d+(\.\d+)?)([BKMGTP]B)$", value.strip(), re.IGNORECASE)
        if not match:
            raise ValueError("Invalid string format")

        number, _, unit = match.groups()
        return int(float(number) * units[unit.upper()])

    def __str__(self) -> str:
        units: list[str] = ["B", "KB", "MB", "GB", "TB", "PB"]
        size: float = float(self.bytes)
        unit_index: int = 0

        while size >= 1024 and unit_index < len(units) - 1:
            size /= 1024
            unit_index += 1

        return f"{size:.2f}{units[unit_index]}"

    def __int__(self) -> int:
        return self.bytes

    def __add__(self, other: Union[int, "Bytes"]) -> "Bytes":
        if isinstance(other, int):
            return Bytes(self.bytes + other)
        elif isinstance(other, Bytes):
            return Bytes(self.bytes + other.bytes)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other: Union[int, "Bytes"]) -> "Bytes":
        if isinstance(other, int):
            return Bytes(self.bytes - other)
        elif isinstance(other, Bytes):
            return Bytes(self.bytes - other.bytes)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other: Union[int, float]) -> "Bytes":
        if isinstance(other, (int, float)):
            return Bytes(int(self.bytes * other))
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other: Union[int, float]) -> "Bytes":
        if isinstance(other, (int, float)):
            return Bytes(int(self.bytes / other))
        else:
            raise TypeError("Unsupported operand type for /")

    def __floordiv__(self, other: Union[int, float]) -> "Bytes":
        if isinstance(other, (int, float)):
            return Bytes(self.bytes // other)
        else:
            raise TypeError("Unsupported operand type for //")
