from aoc21.p12 import parse_input, count_paths


def test_example():
    data = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end
""".strip().splitlines()
    # assert count_paths(parse_input(data), can_visit_twice=False) == 10
    assert count_paths(parse_input(data), can_visit_twice=True) == 36


def test_example_2():
    data = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""".strip().splitlines()
    assert count_paths(parse_input(data), can_visit_twice=False) == 19
    assert count_paths(parse_input(data), can_visit_twice=True) == 103


def test_example_3():
    data = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""".strip().splitlines()
    assert count_paths(parse_input(data), can_visit_twice=False) == 226
    assert count_paths(parse_input(data), can_visit_twice=True) == 3509
