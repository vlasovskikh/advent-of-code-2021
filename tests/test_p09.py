from aoc21.p09 import parse_input, sum_risk_levels, top_3_basin_sizes_multiplied


def test_example():
    data = """
2199943210
3987894921
9856789892
8767896789
9899965678
""".strip().splitlines()
    heightmap = parse_input(data)
    assert sum_risk_levels(heightmap) == 15
    assert top_3_basin_sizes_multiplied(heightmap) == 1134
