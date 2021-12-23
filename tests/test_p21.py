from aoc21.p21 import parse_input, losing_score_by_rolls


def test_example():
    data = """
Player 1 starting position: 4
Player 2 starting position: 8
""".strip().splitlines()
    p1, p2 = parse_input(data)
    assert losing_score_by_rolls(p1, p2) == 739785
