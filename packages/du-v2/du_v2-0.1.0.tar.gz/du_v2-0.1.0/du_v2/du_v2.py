import pwd
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Literal, Optional, Tuple

import tyro
from tqdm import tqdm


@dataclass
class Args:
    dir: Path
    """Directory to check"""
    size_thresh_gb: Optional[float] = 20.0
    """Size threshold in GB at which to stop counting the folder size"""
    time_thresh_sec: Optional[float] = 10.0
    """Time threshold in seconds at which to stop counting the folder size"""
    dates_to_print: List[Literal["created", "modified", "accessed"]] = field(
        default_factory=lambda: []
    )
    """Dates to print for each item in the directory"""
    print_as_calculated: bool = False
    """Print the folder sizes as they are calculated, in addition to at the end"""
    print_below_threshold: bool = True
    """Print files and folders below both thresholds (not just above them)"""
    max_depth: Optional[int] = None
    """Max depth to recursively search subdirectories that were above threshold. None means no recursion beyond the input directory"""
    very_small_thresh_gb: Optional[float] = 0.01
    """Size threshold in GB at which to classify files and folders as very small. These will not be printed"""

    def __post_init__(self) -> None:
        assert self.dir.exists(), f"Directory {self.dir} does not exist"

    @property
    def size_thresh_b(self) -> Optional[float]:
        return (
            self.size_thresh_gb * 1024 * 1024 * 1024
            if self.size_thresh_gb is not None
            else None
        )


def _is_out_of_time(start_time: float, time_threshold_sec: Optional[float]) -> bool:
    return (
        time_threshold_sec is not None and time.time() - start_time > time_threshold_sec
    )


def _is_too_big(total_size_b: float, size_threshold_b: Optional[float]) -> bool:
    return size_threshold_b is not None and total_size_b > size_threshold_b


def get_item_size(
    item: Path, size_threshold_b: Optional[float], time_threshold_sec: Optional[float]
) -> Tuple[float, bool, bool]:
    start_time = time.time()
    if not item.exists():
        total_size_b = 0

    elif not item.is_dir():
        total_size_b = item.stat().st_size

    else:  # item.is_dir()
        total_size_b = 0
        for subitem in item.rglob("*"):
            if not subitem.is_file():
                continue

            total_size_b += subitem.stat().st_size
            is_too_big = _is_too_big(
                total_size_b=total_size_b, size_threshold_b=size_threshold_b
            )
            is_out_of_time = _is_out_of_time(
                start_time=start_time, time_threshold_sec=time_threshold_sec
            )
            if is_too_big or is_out_of_time:
                break

    is_too_big = _is_too_big(
        total_size_b=total_size_b, size_threshold_b=size_threshold_b
    )
    is_out_of_time = _is_out_of_time(
        start_time=start_time, time_threshold_sec=time_threshold_sec
    )
    return total_size_b, is_too_big, is_out_of_time


@dataclass
class ProcessedItem:
    item: Path
    total_size_b: float
    is_too_big: bool
    is_out_of_time: bool
    very_small_thresh_gb: Optional[float]

    @property
    def item_owner(self) -> str:
        try:
            return pwd.getpwuid(self.item.stat().st_uid).pw_name
        except KeyError:
            return "Unknown"

    @property
    def total_size_gb(self) -> float:
        return self.total_size_b / 1024 / 1024 / 1024

    @property
    def creation_time(self) -> str:
        return time.ctime(self.item.stat().st_ctime)

    @property
    def modification_time(self) -> str:
        return time.ctime(self.item.stat().st_mtime)

    @property
    def above_threshold(self) -> bool:
        return self.is_too_big or self.is_out_of_time

    @property
    def is_very_small(self) -> bool:
        return (
            self.very_small_thresh_gb is not None
            and self.total_size_gb < self.very_small_thresh_gb
        )

    def print(
        self, dates_to_print: List[Literal["created", "modified", "accessed"]]
    ) -> None:
        if self.is_very_small:
            return

        print(
            f"{self.item} ({self.item_owner}): {self.total_size_gb:.2f}GB"
            + (" (too big)" if self.is_too_big else "")
            + (" (out of time)" if self.is_out_of_time else "")
        )
        if "created" in dates_to_print:
            print(f"  Created: {self.creation_time}")
        if "modified" in dates_to_print:
            print(f"  Modified: {self.modification_time}")
        if "accessed" in dates_to_print:
            print(f"  Accessed: {time.ctime(self.item.stat().st_atime)}")


def check_item_sizes(
    directory: Path,
    size_threshold_b: Optional[float],
    time_threshold_sec: Optional[float],
    dates_to_print: List[Literal["created", "modified", "accessed"]],
    print_as_calculated: bool,
    print_below_threshold: bool,
    very_small_thresh_gb: Optional[float],
) -> List[ProcessedItem]:
    directory_path = Path(directory)
    item_list = [item for item in directory_path.iterdir()]

    processed_items: List[ProcessedItem] = []
    unprocessed_items = []
    for item in tqdm(item_list, desc=f"Checking items in {directory}"):
        try:
            size, is_too_big, is_out_of_time = get_item_size(
                item=item,
                size_threshold_b=size_threshold_b,
                time_threshold_sec=time_threshold_sec,
            )

            processed_item = ProcessedItem(
                item=item,
                total_size_b=size,
                is_too_big=is_too_big,
                is_out_of_time=is_out_of_time,
                very_small_thresh_gb=very_small_thresh_gb,
            )
            processed_items.append(processed_item)

            if print_as_calculated:
                if processed_item.above_threshold or print_below_threshold:
                    processed_item.print(dates_to_print)
        except PermissionError:
            unprocessed_items.append(item)

            if print_as_calculated:
                print(f"Could not access {item}")

    if len(unprocessed_items) > 0:
        print("\n" + "=" * 80)
        print("Unprocessed items:")
        print("=" * 80 + "\n")
        for item in unprocessed_items:
            print(f"Could not access {item}")

    print("\n" + "=" * 80)
    print("Sorted by size:")
    print("=" * 80 + "\n")
    sorted_processed_items = sorted(
        processed_items,
        key=lambda x: x.total_size_b,
        reverse=False,
    )

    for processed_item in sorted_processed_items:
        if processed_item.above_threshold or print_below_threshold:
            processed_item.print(dates_to_print)
    return sorted_processed_items


def main() -> None:
    args = tyro.cli(tyro.conf.FlagConversionOff[Args])
    if args.max_depth is None:
        check_item_sizes(
            directory=args.dir,
            size_threshold_b=args.size_thresh_b,
            time_threshold_sec=args.time_thresh_sec,
            dates_to_print=args.dates_to_print,
            print_as_calculated=args.print_as_calculated,
            print_below_threshold=args.print_below_threshold,
            very_small_thresh_gb=args.very_small_thresh_gb,
        )
    else:
        directories = [args.dir]
        for depth in range(args.max_depth):
            if len(directories) == 0:
                break

            print(f"\nChecking depth {depth} with {len(directories)} directories...\n")

            next_directories = []
            for directory in directories:
                sorted_processed_items = check_item_sizes(
                    directory=directory,
                    size_threshold_b=args.size_thresh_b,
                    time_threshold_sec=args.time_thresh_sec,
                    dates_to_print=args.dates_to_print,
                    print_as_calculated=args.print_as_calculated,
                    print_below_threshold=args.print_below_threshold,
                    very_small_thresh_gb=args.very_small_thresh_gb,
                )
                next_directories.extend(
                    [
                        processed_item.item
                        for processed_item in sorted_processed_items
                        if processed_item.item.is_dir()
                        and processed_item.above_threshold
                    ]
                )
            directories = next_directories


if __name__ == "__main__":
    main()
