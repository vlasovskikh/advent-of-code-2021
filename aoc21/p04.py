from typing import Iterator, cast

import numpy as np

from aoc21 import utils


def play_bingo(boards: np.ndarray, numbers: list[int]) -> Iterator[tuple[int, int]]:
    """Play bingo on a set of `boards` using `numbers` and return the sum of
    unmarked numbers on the winning board and the last called number.

    `boards` is a 3D-array of all the 2D boards.
    """
    n_boards, n_rows, n_cols = boards.shape
    assert n_rows == n_cols
    bingo = np.full(boards.shape, False)
    playing = np.full(boards.shape, True)
    for number in numbers:
        bingo[boards == number] = True
        for axis in [1, 2]:  # Columns and rows
            complete_lines = np.all(playing & bingo, axis=axis)
            if not np.any(complete_lines):
                continue
            index = winner_index(complete_lines)
            winner = boards[index]
            unmarked = ~bingo[index]
            yield cast(int, np.sum(winner[unmarked])), number
            playing[index] = False
            if not np.any(playing):
                return
    raise ValueError("Unfinished boards, but not numbers left")


def winner_index(complete_lines: np.ndarray) -> int:
    """Index of the winning board from the complete lines.

    `complete_lines` is a 2D-array of (board, axis) with `True` when we have a complete
    line for this axis on this board.
    """
    wins = np.any(complete_lines, axis=1)
    return np.where(wins)[0][0]


def parse_input(lines: list[str]) -> tuple[np.ndarray, list[int]]:
    first, *rest = lines
    numbers = [int(x) for x in first.split(",")]
    boards = []
    board = []
    for line in rest:
        if line:
            board.append([int(x) for x in line.split()])
        elif board:
            boards.append(board)
            board = []
    return np.array(boards), numbers


def main():
    boards, numbers = parse_input(utils.read_input_lines(__file__))
    first, *rest, last = play_bingo(boards, numbers)
    for sum, n in [first, last]:
        print(sum * n)


if __name__ == "__main__":
    main()
