import numpy as np

from aoc21 import utils


def sum_risk_levels(heightmap: list[list[int]]) -> int:
    lows = []
    first_row, last_row = 0, len(heightmap) - 1
    for i, row in enumerate(heightmap):
        first_col, last_col = 0, len(row) - 1
        for j, point in enumerate(row):
            if (
                (i == first_row or point < heightmap[i - 1][j])
                and (i == last_row or point < heightmap[i + 1][j])
                and (j == first_col or point < heightmap[i][j - 1])
                and (j == last_col or point < heightmap[i][j + 1])
            ):
                lows.append(point)
    return sum(p + 1 for p in lows)


def parse_input(lines: list[str]) -> list[list[int]]:
    return np.array([[int(c) for c in line] for line in lines])


def main():
    heightmap = parse_input(utils.read_input_lines(__file__))
    print(sum_risk_levels(heightmap))


if __name__ == "__main__":
    main()
