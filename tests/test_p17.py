from aoc21.p17 import parse_input, shoot


def test_example():
    data = "target area: x=20..30, y=-10..-5".splitlines()
    xs, ys = parse_input(data)
    assert shoot(xs, ys) == (45, 112)
