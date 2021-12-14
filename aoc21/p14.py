import itertools
from typing import cast
from collections import defaultdict

from aoc21 import utils


def substitute(polymer: str, rules: dict[str, str], count: int) -> int:
    first, last = polymer[0], polymer[-1]
    pair_rules = {tuple(k): v for k, v in rules.items()}
    counts: dict[tuple[str, str], int] = {
        cast(tuple[str, str], k): len(list(v))
        for k, v in (itertools.groupby(sorted(utils.sliding_window(polymer, 2))))
    }
    for step in range(count):
        new_counts: dict[tuple[str, str], int] = defaultdict(lambda: 0)
        for k, v in counts.items():
            a, b = k
            c = pair_rules[k]
            new_counts[(a, c)] += v
            new_counts[(c, b)] += v
        counts = new_counts
    return most_common_minus_least_common(first, last, counts)


def most_common_minus_least_common(
    first: str, last: str, counts: dict[tuple[str, str], int]
) -> int:
    cs: dict[str, int] = defaultdict(lambda: 0)
    for k, v in counts.items():
        a, b = k
        cs[a] += v
        cs[b] += v
    cs = {k: v // 2 for k, v in cs.items()}
    cs[first] += 1
    cs[last] += 1
    return max(cs.values()) - min(cs.values())


def parse_input(lines: list[str]) -> tuple[str, dict[str, str]]:
    first, second, *rest = lines
    rules = {k: v for k, v in (line.split(" -> ") for line in rest)}
    return first, rules


def main():
    polymer, rules = parse_input(utils.read_input_lines(__file__))
    print(substitute(polymer, rules, 10))
    print(substitute(polymer, rules, 40))


if __name__ == "__main__":
    main()
