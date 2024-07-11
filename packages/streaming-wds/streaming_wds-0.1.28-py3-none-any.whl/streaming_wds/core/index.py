import gzip
import json
import logging
from dataclasses import dataclass
from typing import List

logger = logging.getLogger(__name__)


@dataclass
class ShardIndex:
    key: str
    num_samples: int

    def to_dict(self):
        return {
            "key": self.key,
            "num_samples": self.num_samples,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            key=data["key"],
            num_samples=data["num_samples"],
        )


@dataclass
class DatasetIndex:
    num_shards: int
    num_items: int
    shards: List[ShardIndex]

    @property
    def shard_keys(self) -> str:
        return [s.key for s in self.shards]

    def to_dict(self):
        return {
            "num_shards": self.num_shards,
            "num_items": self.num_items,
            "shards": [s.to_dict() for s in self.shards],
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            num_shards=data["num_shards"],
            num_items=data["num_items"],
            shards=[ShardIndex.from_dict(s) for s in data["shards"]],
        )

    def encode(self):
        return gzip.compress(json.dumps(self.to_dict()).encode())

    @classmethod
    def decode(cls, data: bytes):
        return cls.from_dict(json.loads(gzip.decompress(data).decode()))
