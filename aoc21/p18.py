from __future__ import annotations

import itertools
import json
from typing import Any

from aoc21 import utils


class Number:
    xs: list

    def __init__(self, xs: list) -> None:
        self.xs = reduce(xs)

    def __repr__(self) -> str:
        return f"Number({self.xs!r})"

    def __add__(self, other: Number) -> Number:
        return Number([self.xs, other.xs])

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Number) and self.xs == other.xs

    def magnitude(self) -> int:
        return magnitude(self.xs)


def magnitude(e: list | int) -> int:
    if isinstance(e, int):
        return e
    elif isinstance(e, list):
        a, b = e
        return magnitude(a) * 3 + magnitude(b) * 2


def reduce(xs: list) -> list:
    while True:
        new = explode(xs)
        if new != xs:
            xs = new
            continue
        new = split(xs)
        if new != xs:
            xs = new
            continue
        return xs


def explode(xs: list) -> list:
    res, _, _ = dive(xs)
    if isinstance(res, int):
        raise TypeError(f"Got integer result of explosion instead of list: {res}")
    return res


def dive(xs: list, nested: int = 1) -> tuple[list | int, int | None, int | None]:
    a, b = xs

    if nested > 4:
        return 0, a, b

    if isinstance(a, list):
        new_a, left, right = dive(a, nested + 1)
        if right is not None:
            new_b = add_leftmost(b, right)
            return [new_a, new_b], left, None
        if left is not None:
            return [new_a, b], left, None
    else:
        new_a = a

    if new_a != a:
        return [new_a, b], None, None

    if isinstance(b, list):
        new_b, left, right = dive(b, nested + 1)
        if left is not None:
            new_a = add_rightmost(a, left)
            return [new_a, new_b], None, right
        if right is not None:
            return [a, new_b], None, right
    else:
        new_b = b

    return [new_a, new_b], None, None


def add_rightmost(e: list | int, value: int) -> list | int:
    if isinstance(e, int):
        return e + value
    elif isinstance(e, list):
        a, b = e
        new_b = add_rightmost(b, value)
        return [a, new_b]


def add_leftmost(e: list | int, value: int) -> list | int:
    if isinstance(e, int):
        return e + value
    elif isinstance(e, list):
        a, b = e
        new_a = add_leftmost(a, value)
        return [new_a, b]


def split(xs: list) -> list:
    a, b = xs
    if isinstance(a, int) and a >= 10:
        div, mod = divmod(a, 2)
        return [[div, div + mod], b]
    elif isinstance(a, list):
        new_a = split(a)
        if new_a != a:
            return [new_a, b]
    if isinstance(b, int) and b >= 10:
        div, mod = divmod(b, 2)
        return [a, [div, div + mod]]
    elif isinstance(b, list):
        new_b = split(b)
        if new_b != b:
            return [a, new_b]
    return [a, b]


def magnitude_of_sum(ns: list[Number]) -> int:
    return sum(ns[1:], ns[0]).magnitude()


def max_magnitude_of_pairs(ns: list[Number]) -> int:
    return max((a + b).magnitude() for a, b in itertools.permutations(ns, 2))


def parse_input(lines: list[str]) -> list[Number]:
    return [Number(json.loads(line)) for line in lines]


def main() -> None:
    numbers = parse_input(utils.read_input_lines(__file__))
    print(magnitude_of_sum(numbers))
    print(max_magnitude_of_pairs(numbers))


if __name__ == "__main__":
    main()
