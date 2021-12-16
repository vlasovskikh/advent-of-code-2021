from __future__ import annotations

import heapq
import sys
from collections import defaultdict


from aoc21 import utils

Point = tuple[int, int]


def lowest_total_risk(cavern: list[list[int]]) -> int:
    n_rows, n_cols = len(cavern), len(cavern[0])
    risks: dict[Point, int] = defaultdict(lambda: sys.maxsize)
    risks[(0, 0)] = 0
    traceback: dict[Point, Point] = {}
    queue = [(0, (0, 0))]
    while queue:
        risk, point = heapq.heappop(queue)
        if point == (n_cols - 1, n_rows - 1):
            return total_risk(point, traceback, cavern)
        for step in next_steps(point, n_rows, n_cols):
            x, y = point
            sx, sy = step
            step_risk = risks[point] + cavern[sy][sx]
            if step_risk < risks[step]:
                traceback[step] = point
                risks[step] = step_risk
                estimate = step_risk + (n_cols - sx - 1) + (n_rows - sy - 1)
                heapq.heappush(queue, (estimate, step))
    raise ValueError("No path found")


def next_steps(point: Point, n_rows: int, n_cols: int) -> list[Point]:
    x, y = point
    candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(x, y) for x, y in candidates if (0 <= x < n_cols and 0 <= y < n_rows)]


def total_risk(
    point: Point,
    traceback: dict[Point, Point],
    cavern: list[list[int]],
) -> int:
    x, y = point
    s = cavern[y][x]
    while (x, y) in traceback:
        x, y = traceback[(x, y)]
        s += cavern[y][x]
    return s - cavern[0][0]


def parse_input(lines: list[str]) -> list[list[int]]:
    return [[int(c) for c in line] for line in lines]


def main():
    cavern = parse_input(utils.read_input_lines(__file__))
    print(lowest_total_risk(cavern))


if __name__ == "__main__":
    main()
