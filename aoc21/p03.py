from typing import Callable

from aoc21 import utils
import numpy as np


def gamma_and_epsilon(array: np.ndarray) -> tuple[int, int]:
    """Calculate gamma and epsilon for a submarine diagnostic report."""
    if len(array) == 0:
        raise ValueError("Empty array")
    diff = np.sum(array == 1, axis=0) - np.sum(array == 0, axis=0)
    g_bits = list(diff >= 0)
    e_bits = list(diff < 0)
    return bools_to_int(g_bits), bools_to_int(e_bits)


def bools_to_int(xs: list[bool]) -> int:
    """Convert a boolean list into the corresponding integer using base 2."""
    return int("".join("1" if x else "0" for x in xs), base=2)


def o2_and_co2(array: np.ndarray) -> tuple[int, int]:
    """Calculate o2 and co2 ratings for a submarine diagnostic report."""
    o2 = life_support(array, o2_criteria)
    co2 = life_support(array, co2_criteria)
    return o2, co2


def o2_criteria(column: np.ndarray) -> int:
    """The criteria for o2: the most common value in the column."""
    return 1 if np.sum(column == 1) >= np.sum(column == 0) else 0


def co2_criteria(column: np.ndarray) -> int:
    """The criteria for co2: the least common value in the column."""
    return 0 if np.sum(column == 0) <= np.sum(column == 1) else 1


def life_support(array: np.ndarray, bit_criteria: Callable[[np.ndarray], int]) -> int:
    """Calculate a life support rating for a report based on a custom criteria.

    The criteria determines which bits from the column to keep for subsequent columns.
    """
    _, ncols = array.shape
    for i in range(ncols):
        column = array[:, i]
        bit = bit_criteria(column)
        column_mask = column == bit
        mask = np.tile(column_mask[:, None], [1, ncols])
        masked = array[mask]
        array = masked.reshape(masked.size // ncols, ncols)
        if array.shape[0] == 1:
            return bools_to_int(list(array[0] == 1))
    raise ValueError("No matching row found")


def parse_input(lines: list[str]) -> np.ndarray:
    return np.array([[int(c) for c in line] for line in lines])


if __name__ == "__main__":
    array = parse_input(utils.read_input_lines(__file__))
    g, e = gamma_and_epsilon(array)
    print(g * e)
    o2, co2 = o2_and_co2(array)
    print(o2 * co2)
