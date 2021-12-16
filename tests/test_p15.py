from aoc21.p15 import parse_input, lowest_total_risk, extend_cavern


def test_example():
    data = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""".strip().splitlines()
    assert lowest_total_risk(parse_input(data)) == 40
    assert lowest_total_risk(extend_cavern(parse_input(data))) == 315
