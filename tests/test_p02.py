from aoc21.p02 import execute_submarine_commands


def test_empty():
    assert execute_submarine_commands([], use_aim=False) == (0, 0)
    assert execute_submarine_commands([], use_aim=True) == (0, 0)


def test_single_forward():
    assert (
        execute_submarine_commands(
            [
                ("forward", 5),
            ],
            use_aim=False,
        )
        == (5, 0)
    )
    assert (
        execute_submarine_commands(
            [
                ("forward", 5),
            ],
            use_aim=True,
        )
        == (5, 0)
    )


def test_single_down():
    assert (
        execute_submarine_commands(
            [
                ("down", 5),
            ],
            use_aim=False,
        )
        == (0, 5)
    )
    assert (
        execute_submarine_commands(
            [
                ("down", 5),
            ],
            use_aim=True,
        )
        == (0, 0)
    )


def test_single_up():
    assert (
        execute_submarine_commands(
            [
                ("up", 5),
            ],
            use_aim=False,
        )
        == (0, -5)
    )
    assert (
        execute_submarine_commands(
            [
                ("up", 5),
            ],
            use_aim=True,
        )
        == (0, 0)
    )


def test_simple_combination():
    assert (
        execute_submarine_commands(
            [
                ("forward", 3),
                ("down", 4),
            ],
            use_aim=False,
        )
        == (3, 4)
    )
    assert (
        execute_submarine_commands(
            [
                ("forward", 3),
                ("down", 4),
            ],
            use_aim=True,
        )
        == (3, 0)
    )


def test_complex_combination():
    assert (
        execute_submarine_commands(
            [
                ("forward", 3),
                ("down", 4),
                ("forward", 5),
                ("up", 2),
            ],
            use_aim=False,
        )
        == (8, 2)
    )
    assert (
        execute_submarine_commands(
            [
                ("forward", 3),
                ("down", 4),
                ("forward", 5),
                ("up", 2),
            ],
            use_aim=True,
        )
        == (8, 20)
    )
