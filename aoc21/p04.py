from typing import Iterator

import numpy as np

from aoc21 import utils


def play_bingo(boards: np.ndarray, numbers: list[int]) -> Iterator[tuple[int, int]]:
    """Play bingo on a set of `boards` using `numbers` and return the sum of
    unmarked numbers on the winning board and the last called number.

    `boards` is a 3D-array of all the 2D boards.
    """
    n_boards, n_rows, n_cols = boards.shape
    assert n_rows == n_cols
    win_combination = np.full(n_rows, True)
    bingo = np.full(boards.shape, False)
    playing = np.full(boards.shape, True)
    for number in numbers:
        bingo[boards == number] = True
        for axis in [1, 2]:  # Columns and rows
            win_arrays = np.all((bingo & playing) == win_combination, axis=axis)
            if np.any(win_arrays):
                index = win_index(win_arrays)
                yield sum_unmarked(boards, bingo, index), number
                playing[index] = False
                if not np.any(playing):
                    return
    raise ValueError("Unfinished boards, but not numbers left")


def sum_unmarked(boards: np.ndarray, bingo: np.ndarray, index: int) -> int:
    """Sum the unmarked number on the board by its index.

    `bingo` is a 3D-array of called check marks `True`. It has the same shape as
    `boards`.
    """
    win_board = boards[index]
    win_bingo = bingo[index]
    unmarked = ~win_bingo
    return int(np.sum(win_board[unmarked]))


def win_index(win_arrays: np.ndarray) -> int:
    """Index of the winning board from the winning arrays.

    `win_arrays` is a 2D-array of (board, axis) with `True` when we have a winning
    combination for this axis on this board.
    """
    win_boards = np.any(win_arrays, axis=1)
    return np.where(win_boards)[0][0]


def parse_input(lines: list[str]) -> tuple[np.ndarray, list[int]]:
    first = lines[0]
    rest = [line.strip() for line in lines[1:]]
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
    winners = list(play_bingo(boards, numbers))
    first_sum, first_n = winners[0]
    print(first_sum * first_n)
    last_sum, last_n = winners[-1]
    print(last_sum * last_n)


if __name__ == "__main__":
    main()
