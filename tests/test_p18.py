from aoc21.p18 import Number, parse_input, magnitude_of_sum, max_magnitude_of_pairs


def test_simple_add():
    x = Number([1, 1])
    y = Number([2, 2])
    assert x + y == Number([[1, 1], [2, 2]])


def test_add_1():
    x = Number([[[[4, 3], 4], 4], [7, [[8, 4], 9]]])
    y = Number([1, 1])
    assert x + y == Number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])


def test_mag_1():
    assert Number([[1, 2], [[3, 4], 5]]).magnitude() == 143


def test_mag_2():
    assert Number([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]).magnitude() == 1384


def test_sum_1():
    data = """
[1,1]
[2,2]
[3,3]
[4,4]
""".strip().splitlines()
    ns = parse_input(data)
    assert sum(ns[1:], ns[0]) == Number([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])


def test_sum_2():
    data = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
""".strip().splitlines()
    ns = parse_input(data)
    assert sum(ns[1:], ns[0]) == Number([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])


def test_sum_3():
    data = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
""".strip().splitlines()
    ns = parse_input(data)
    assert sum(ns[1:], ns[0]) == Number([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])


def test_sum_two_large_numbers():
    a = Number([[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]])
    b = Number([[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]])
    assert a + b == Number(
        [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]]
    )


def test_sum_4():
    data = """
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
""".strip().splitlines()
    ns = parse_input(data)

    s = ns[0]
    for n in ns[1:]:
        s += n
        print(s)

    assert s == Number(
        [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
    )


def test_example():
    data = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
""".strip().splitlines()
    ns = parse_input(data)
    assert magnitude_of_sum(ns) == 4140
    assert max_magnitude_of_pairs(ns) == 3993
