from aoc21.p06 import parse_input, model_fish


def test_example_18():
    data = "3,4,3,1,2".splitlines()
    assert model_fish(parse_input(data), 18) == 26


def test_example_80():
    data = "3,4,3,1,2".splitlines()
    assert model_fish(parse_input(data), 80) == 5934
