import itertools
from typing import TypeVar, Iterable

from aoc21 import utils


def count_sliding_window_depth_increases(measurements: list[int]) -> int:
    """Count the number of times a depth measurement increases from the previous
    measurement using a sliding window of 3 measurements.
    """
    triples = sliding_window(measurements, 3)
    sums = (sum(triple) for triple in triples)
    sum_pairs = sliding_window(sums, 2)
    increases = (1 for x, y in sum_pairs if x < y)
    return sum(increases)


T = TypeVar("T")


def sliding_window(xs: Iterable[T], n: int) -> Iterable[tuple[T, ...]]:
    """Return a sliding window of size `n` for the specified iterable."""
    iterators = itertools.tee(xs, n)
    for shift_count, iterator in enumerate(iterators):
        for _ in range(shift_count):
            next(iterator, None)
    return zip(*iterators)


def parse_input(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]


if __name__ == "__main__":
    data = parse_input(utils.read_input_lines(__file__))
    print(count_sliding_window_depth_increases(data))
