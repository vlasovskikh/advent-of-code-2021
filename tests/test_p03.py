import pytest

from aoc21.p03 import gamma_and_epsilon, o2_and_co2, parse_input


def b(s):
    return int(s, base=2)


def test_empty():
    with pytest.raises(ValueError):
        gamma_and_epsilon(parse_input([]))


def test_single():
    assert gamma_and_epsilon(parse_input(["01"])) == (b("01"), b("10"))


def test_2_equal():
    assert (
        gamma_and_epsilon(
            parse_input(
                [
                    "01",
                    "01",
                ]
            )
        )
        == (b("01"), b("10"))
    )


def test_3_with_majority():
    assert (
        gamma_and_epsilon(
            parse_input(
                [
                    "01",
                    "01",
                    "10",
                ]
            )
        )
        == (b("01"), b("10"))
    )


def test_4_with_1_equal():
    assert (
        gamma_and_epsilon(
            parse_input(
                [
                    "01",
                    "01",
                    "10",
                    "00",
                ]
            )
        )
        == (b("01"), b("10"))
    )


def test_example():
    assert (
        gamma_and_epsilon(
            parse_input(
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
        )
        == (b("10110"), b("01001"))
    )


def test_o2_empty():
    with pytest.raises(ValueError):
        o2_and_co2(parse_input([]))


def test_o2_no_lines_with_0_for_co2():
    with pytest.raises(ValueError):
        o2_and_co2(parse_input(["1010"]))


def test_o2_2_values():
    assert o2_and_co2(parse_input(["01", "11"])) == (b("11"), b("01"))


def test_o2_3_values():
    assert o2_and_co2(parse_input(["01", "10", "11"])) == (b("11"), b("01"))


def test_first_3_from_example():
    assert (
        o2_and_co2(
            parse_input(
                [
                    "00100",
                    "11110",
                    "10110",
                ]
            )
        )
        == (b("11110"), b("00100"))
    )
