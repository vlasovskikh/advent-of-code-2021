import pytest

from aoc21.p03 import gamma_and_epsilon


def b(s):
    return int(s, base=2)


def test_empty():
    assert gamma_and_epsilon([]) == (0, 0)


def test_single():
    assert gamma_and_epsilon(["01"]) == (b("01"), b("10"))


def test_2_equal():
    assert (
        gamma_and_epsilon(
            [
                "01",
                "01",
            ]
        )
        == (b("01"), b("10"))
    )


def test_3_with_majority():
    assert (
        gamma_and_epsilon(
            [
                "01",
                "01",
                "10",
            ]
        )
        == (b("01"), b("10"))
    )


def test_4_with_1_equal():
    with pytest.raises(ValueError):
        assert gamma_and_epsilon(
            [
                "01",
                "01",
                "10",
                "00",
            ]
        )


def test_example():
    assert (
        gamma_and_epsilon(
            [
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ]
        )
        == (b("10110"), b("01001"))
    )
