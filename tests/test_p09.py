from aoc21.p09 import parse_input, sum_risk_levels


def test_example():
    data = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip().splitlines()
    assert sum_risk_levels(parse_input(data)) == 15
