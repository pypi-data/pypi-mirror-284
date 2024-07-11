import argparse
from typing import Optional

from tqdm import tqdm

from streaming_wds import StreamingDataLoader, StreamingWebDataset
from streaming_wds.utils import clean_stale_cache


def main(
    remote: str,
    split: Optional[str] = None,
    batch_size: int = 1,
    dataset_threads: int = 8,
    dataloader_workers: int = 2,
    aws_profile: str = "default",
    memory_buffer_limit_bytes: str = "10GB",
    file_cache_limit_bytes: str = "10GB",
):
    clean_stale_cache(remote)

    ds = StreamingWebDataset(
        remote,
        split=split,
        max_workers=dataset_threads,
        profile=aws_profile,
        memory_buffer_limit_bytes=memory_buffer_limit_bytes,
        file_cache_limit_bytes=file_cache_limit_bytes,
    )
    dl = StreamingDataLoader(ds, batch_size=batch_size, num_workers=dataloader_workers)

    num_samples = 0
    for _ in tqdm(dl):
        num_samples += 1

    print(f"Number of samples: {num_samples}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("remote", type=str, help="The S3 URI of the dataset")
    parser.add_argument(
        "--split",
        type=str,
        default=None,
        help="The dataset split (e.g., 'train', 'val', 'test')",
    )
    parser.add_argument(
        "--threads", type=int, default=8, help="Number of threads for the dataset"
    )
    parser.add_argument(
        "--workers", type=int, default=8, help="Number of workers for the dataloader"
    )
    parser.add_argument(
        "--aws_profile",
        type=str,
        default="default",
        help="The AWS profile to use for authentication",
    )
    parser.add_argument(
        "--memory_buffer_limit",
        type=str,
        default="10GB",
        help="The memory buffer limit in bytes",
    )
    parser.add_argument(
        "--file_cache_limit",
        type=str,
        default="10GB",
        help="The file cache limit in bytes",
    )

    args = parser.parse_args()
    main(
        args.remote,
        split=args.split,
        dataset_threads=args.threads,
        dataloader_workers=args.workers,
        aws_profile=args.aws_profile,
        memory_buffer_limit_bytes=args.memory_buffer_limit,
        file_cache_limit_bytes=args.file_cache_limit,
    )
