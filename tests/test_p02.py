from aoc21.p02 import execute_submarine_commands


def test_empty():
    assert execute_submarine_commands([]) == (0, 0)


def test_single_forward():
    assert (
        execute_submarine_commands(
            [
                ("forward", 5),
            ]
        )
        == (5, 0)
    )


def test_single_down():
    assert (
        execute_submarine_commands(
            [
                ("down", 5),
            ]
        )
        == (0, 5)
    )


def test_single_up():
    assert (
        execute_submarine_commands(
            [
                ("up", 5),
            ]
        )
        == (0, -5)
    )


def test_simple_combination():
    assert (
        execute_submarine_commands(
            [
                ("forward", 3),
                ("down", 4),
            ]
        )
        == (3, 4)
    )


def test_complex_combination():
    assert (
        execute_submarine_commands(
            [
                ("forward", 3),
                ("down", 4),
                ("forward", 5),
                ("up", 2),
            ]
        )
        == (8, 2)
    )
