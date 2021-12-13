import numpy as np

from aoc21.p13 import parse_input, fold_array


def test_example():
    data = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
""".strip().splitlines()
    array, folds = parse_input(data)
    first, *rest = folds
    assert np.sum(fold_array(array, [first])) == 17
