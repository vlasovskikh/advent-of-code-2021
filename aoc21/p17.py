import re
from typing import Iterable

from aoc21 import utils

Range = tuple[int, int]
Point = tuple[int, int]


def trajectory(vx: int, vy: int) -> Iterable[Point]:
    x, y = 0, 0
    while True:
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1
        yield x, y


def sign(x: int) -> int:
    return 1 if x > 0 else -1 if x < 0 else 0


def check_target(points: Iterable[Point], xs: Range, ys: Range) -> tuple[int, int]:
    xa, xb = xs
    ya, yb = ys
    max_y = ya
    prev_x = 0
    for x, y in points:
        if y > max_y:
            max_y = y
        if xa <= x <= xb and ya <= y <= yb:
            return 0, max_y
        elif y < ya:
            return -1, max_y
        elif x > xb:
            return -1, max_y
        elif x == prev_x and x < xa:
            return 1, max_y
        prev_x = x
    return -1, max_y


def shoot(xs: Range, ys: Range) -> tuple[int, int]:
    xa, xb = xs
    ya, yb = ys
    max_heights = []
    velocities = set()
    for vx in range(1, xb + 1):
        for vy in range(min(0, ya), yb + 1 if ya > 0 else -ya):
            res, max_y = check_target(trajectory(vx, vy), xs, ys)
            if res == 0:
                max_heights.append(max_y)
                velocities.add((vx, vy))
            elif res > 0:
                break
    return max(max_heights), len(velocities)


def parse_input(lines: list[str]) -> tuple[Range, Range]:
    m = re.match(r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", lines[0])
    if not m:
        raise ValueError(f"Cannot parse line: {lines[0]!r}")
    xa, xb, ya, yb = [int(s) for s in m.groups()]
    return (xa, xb), (ya, yb)


def main() -> None:
    xs, ys = parse_input(utils.read_input_lines(__file__))
    highest, velocities = shoot(xs, ys)
    print(highest)
    print(velocities)


if __name__ == "__main__":
    main()
