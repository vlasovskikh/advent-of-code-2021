from aoc21.p07 import parse_input, minimize_fuel


def test_example():
    crabs = parse_input(
        """
16,1,2,0,4,2,7,1,2,14
""".strip().splitlines()
    )
    assert minimize_fuel(crabs) == 37
