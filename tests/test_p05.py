from aoc21.p05 import parse_input, dangerous_areas


def test_example():
    data = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""".strip().splitlines()
    assert dangerous_areas(parse_input(data), diagonals=False) == 5
    assert dangerous_areas(parse_input(data), diagonals=True) == 12


def test_diagonal_cross():
    data = """
0,0 -> 2,2
0,2 -> 2,0
""".strip().splitlines()
    assert dangerous_areas(parse_input(data), diagonals=True) == 1


def test_normal_and_diagonal_crosses():
    data = """
0,0 -> 2,2
0,2 -> 2,0
0,1 -> 2,1
1,0 -> 1,2
""".strip().splitlines()
    assert dangerous_areas(parse_input(data), diagonals=True) == 1


def test_diagonal_cross_backwards():
    data = """
2,2 -> 0,0
2,0 -> 0,2
""".strip().splitlines()
    assert dangerous_areas(parse_input(data), diagonals=True) == 1


def test_normal_cross():
    data = """
1,0 -> 1,2
0,1 -> 2,1
""".strip().splitlines()
    assert dangerous_areas(parse_input(data), diagonals=True) == 1


def test_normal_cross_backwards():
    data = """
1,2 -> 1,0
2,1 -> 0,1
""".strip().splitlines()
    assert dangerous_areas(parse_input(data), diagonals=True) == 1
