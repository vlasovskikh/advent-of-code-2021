from aoc21.p14 import parse_input, substitute


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
    assert substitute(polymer, rules, 10) == 1588


def test_substitute_1():
    data = """
AB

AB -> C
""".strip().splitlines()
    polymer, rules = parse_input(data)
    assert substitute(polymer, rules, 1) == 0


def test_substitute_3():
    data = """
AB

AB -> C
AC -> C
CB -> B
CC -> C
BB -> C
""".strip().splitlines()
    polymer, rules = parse_input(data)
    assert substitute(polymer, rules, 3) == 4
