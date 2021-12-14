from aoc21.p14 import parse_input, substitute, most_common_minus_least_common


def test_example():
    # noinspection SpellCheckingInspection
    data = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip().splitlines()
    polymer, rules = parse_input(data)
    assert most_common_minus_least_common(substitute(polymer, rules, 10)) == 1588
