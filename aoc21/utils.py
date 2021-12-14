import itertools
import os
from pathlib import Path
from typing import TypeVar, Iterable


def read_input_lines(module_path: str) -> list[str]:
    """Read lines of the input file that corresponds to the module name."""
    with open(input_file_path(module_path), "r") as fd:
        return [s.strip() for s in fd.readlines()]


def input_file_path(module_path: str) -> Path:
    """Input file path from `data/` that corresponds to the module name."""
    p = Path(module_path)  # "/Users/vlan/exp/2021/aoc21/p01a.py"
    module_name, _ = os.path.splitext(p.name)
    return p.parent / ".." / "data" / f"{module_name}.txt"


T = TypeVar("T")


def sliding_window(xs: Iterable[T], n: int) -> Iterable[tuple[T, ...]]:
    """Return a sliding window of size `n` for the specified iterable."""
    iterators = itertools.tee(xs, n)
    for shift_count, iterator in enumerate(iterators):
        for _ in range(shift_count):
            next(iterator, None)
    return zip(*iterators)
