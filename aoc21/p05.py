import itertools
import re

import numpy as np

from aoc21 import utils

Line = tuple[int, int, int, int]


def dangerous_areas(lines: list[Line], *, diagonals: bool) -> int:
    """Find all the dangerous areas areas where at least two lines interect.

    Set `diagonals` to `True` to count diagonals too, otherwise it's only horizontal
    and vertical lines.
    """
    field = np.full(dimentions(lines), 0)
    for x1, y1, x2, y2 in lines:
        if x1 == x2 or y1 == y2:
            field[slice(*slice_tuple(y1, y2)), slice(*slice_tuple(x1, x2))] += 1
        elif diagonals:
            x_slice = slice_tuple(x1, x2, for_range=True)
            y_slice = slice_tuple(y1, y2, for_range=True)
            for x, y in zip(range(*x_slice), range(*y_slice)):
                field[y, x] += 1
    return len(field[field >= 2])


def slice_tuple(x1: int, x2: int, *, for_range: bool = False) -> tuple[int, int, int]:
    """Return (start, stop, step) for the specified range of `x1`, `x2`.

    `x1` and `x2` can be specified in any order.

    `range()` uses `stop = -1` to stop at the first element, while `slice()` uses
    `None` for this purpose. You can specify the desired behaviour using `for_range`.
    """
    sign = np.sign(x2 - x1) if x1 != x2 else 1
    stop = x2 + sign
    return x1, stop if stop >= 0 or for_range else None, sign


def dimentions(lines: list[Line]) -> tuple[int, int]:
    """The dimentions of a field sufficient to accomodate these `lines`."""
    x = max(itertools.chain((line[0] for line in lines), (line[2] for line in lines)))
    y = max(itertools.chain((line[1] for line in lines), (line[3] for line in lines)))
    return x + 1, y + 1


def parse_input(lines: list[str]) -> list[Line]:
    res = []
    for line in lines:
        if m := re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line):
            x1, y1, x2, y2 = [int(g) for g in m.groups()]
            res.append((x1, y1, x2, y2))
    return res


def main():
    lines = parse_input(utils.read_input_lines(__file__))
    print(dangerous_areas(lines, diagonals=False))
    print(dangerous_areas(lines, diagonals=True))


if __name__ == "__main__":
    main()
