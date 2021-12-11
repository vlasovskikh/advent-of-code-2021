import numpy as np

from aoc21 import utils


def count_flashes(array: np.ndarray) -> int:
    array = array.copy()
    count = 0
    for _ in range(100):
        flashes: set[tuple[int, int]] = set()
        array += 1
        while new := new_flashes(array, flashes):
            flashes |= new
            for x, y in new:
                ns = neighbors(array, x, y)
                ns += 1
        count += len(flashes)
        array[array > 9] = 0
    return count


def new_flashes(
    array: np.ndarray, flashes: set[tuple[int, int]]
) -> set[tuple[int, int]]:
    rows, cols = np.where(array > 9)
    all_flashes = set(zip(rows, cols))
    return all_flashes - flashes


def neighbors(array: np.ndarray, x: int, y: int) -> np.ndarray:
    n_rows, n_cols = array.shape
    rows = slice(max(0, x - 1), min(x + 2, n_rows))
    cols = slice(max(0, y - 1), min(y + 2, n_cols))
    return array[rows, cols]


def main():
    array = parse_input(utils.read_input_lines(__file__))
    print(count_flashes(array))


def parse_input(lines: list[str]) -> np.ndarray:
    return np.array([[int(c) for c in line] for line in lines])


if __name__ == "__main__":
    main()
