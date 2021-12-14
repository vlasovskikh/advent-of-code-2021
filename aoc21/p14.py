import itertools

from aoc21 import utils


def substitute(polymer: str, rules: dict[str, str], count: int) -> str:
    sequence = list(polymer)
    pair_rules = {tuple(k): v for k, v in rules.items()}
    for step in range(count):
        pairs = utils.sliding_window(sequence, 2)
        insertions = [pair_rules[pair] for pair in pairs]
        for i, c in enumerate(insertions):
            sequence.insert(i * 2 + 1, c)
    return "".join(sequence)


def most_common_minus_least_common(polymer: str) -> int:
    values = [len(list(g)) for c, g in itertools.groupby(sorted(polymer))]
    return max(values) - min(values)


def parse_input(lines: list[str]) -> tuple[str, dict[str, str]]:
    first, second, *rest = lines
    rules = {k: v for k, v in (line.split(" -> ") for line in rest)}
    return first, rules


def main():
    polymer, rules = parse_input(utils.read_input_lines(__file__))
    print(most_common_minus_least_common(substitute(polymer, rules, 10)))


if __name__ == "__main__":
    main()
