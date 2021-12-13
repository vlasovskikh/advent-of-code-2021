import re

import numpy as np
from aoc21 import utils


def fold_array(array: np.ndarray, folds: list[tuple[str, int]]) -> np.ndarray:
    for coord, pos in folds:
        if coord == "x":
            right = array[:, pos + 1 :]
            array = array[:, :pos] | right[:, ::-1]
        elif coord == "y":
            bottom = array[pos + 1 :, :]
            array = array[:pos, :] | bottom[::-1, :]
        else:
            raise ValueError(f"Unknown coordinate: '{coord}'")
    return array


def parse_input(lines: list[str]) -> tuple[np.ndarray, list[tuple[str, int]]]:
    empty = lines.index("")
    dot_lines, fold_lines = lines[:empty], lines[empty + 1 :]
    dots = [(int(x), int(y)) for x, y in [s.split(",") for s in dot_lines]]
    max_y, max_x = max(y for x, y in dots), max(x for x, y in dots)
    folds = [(c, int(p)) for c, p in [parse_fold_line(s) for s in fold_lines]]
    max_x_fold = max(p for c, p in folds if c == "x")
    max_y_fold = max(p for c, p in folds if c == "y")
    n_rows = max(max_y + 1, max_y_fold * 2 + 1)
    n_cols = max(max_x + 1, max_x_fold * 2 + 1)
    array = np.full((n_rows, n_cols), False)
    for x, y in dots:
        array[y, x] = True

    return array, folds


def parse_fold_line(line: str) -> tuple[str, int]:
    if m := re.match(r"fold along ([xy])=(\d+)", line):
        coord, pos = m.groups()
        return coord, int(pos)
    raise ValueError(f"Cannot parse fold line: {line}")


def main():
    array, folds = parse_input(utils.read_input_lines(__file__))
    first, *rest = folds
    print(np.sum(fold_array(array, [first])))
    folded = fold_array(array, folds)
    res = np.full(folded.shape, ".")
    res[folded] = "#"
    for line in res.tolist():
        print("".join(line))


if __name__ == "__main__":
    main()
