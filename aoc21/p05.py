import itertools
import re
from typing import Iterator

import numpy as np

from aoc21 import utils

Line = tuple[int, int, int, int]


def dangerous_areas(lines: list[Line]) -> int:
    field = np.full(dimentions(lines), 0)
    for x1, y1, x2, y2 in horizontal_and_vertical(lines):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        field[y1 : y2 + 1, x1 : x2 + 1] += 1  # noqa: E203
    return len(field[field >= 2])


def dimentions(lines: list[Line]) -> tuple[int, int]:
    x = max(itertools.chain((line[0] for line in lines), (line[2] for line in lines)))
    y = max(itertools.chain((line[1] for line in lines), (line[3] for line in lines)))
    return x + 1, y + 1


def horizontal_and_vertical(lines: list[Line]) -> Iterator[Line]:
    for x1, y1, x2, y2 in lines:
        if x1 == x2 or y1 == y2:
            yield x1, y1, x2, y2


def parse_input(lines: list[str]) -> list[Line]:
    res = []
    for line in lines:
        if m := re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line):
            x1, y1, x2, y2 = [int(g) for g in m.groups()]
            res.append((x1, y1, x2, y2))
    return res


def main():
    lines = parse_input(utils.read_input_lines(__file__))
    print(dangerous_areas(lines))


if __name__ == "__main__":
    main()
