import numpy as np
from aoc21 import utils


def play_bingo(boards: np.ndarray, numbers: list[int]) -> tuple[int, int]:
    """Play bingo on a set of `boards` using `numbers` and return the sum of
    unmarked numbers on the winning board and the last called number.

    `boards` is a 3D-array of all the 2D boards.
    """
    n_boards, n_rows, n_cols = boards.shape
    assert n_rows == n_cols
    win_combination = np.full(n_rows, True)
    bingo = np.full(boards.shape, False)
    for number in numbers:
        bingo[boards == number] = True
        for axis in [1, 2]:  # Columns and rows
            win_arrays = np.all(bingo == win_combination, axis=axis)
            if np.any(win_arrays):
                return sum_unmarked_for_winner(boards, bingo, win_arrays), number
    raise ValueError("No winning board")


def sum_unmarked_for_winner(
    boards: np.ndarray, bingo: np.ndarray, win_arrays: np.ndarray
) -> int:
    """Sum the unmarked number on the winning board, given the winning arrays.

    `bingo` is a 3D-array of called check marks `True`. It has the same shape as
    `boards`.

    `win_arrays` is a 2D-array of (board, axis) with `True` when we have a winning
    combination for this axis on this board.
    """
    win_boards = np.any(win_arrays, axis=1)
    win_index = np.where(win_boards)[0][0]
    win_board = boards[win_index]
    win_bingo = bingo[win_index]
    unmarked = ~win_bingo
    return int(np.sum(win_board[unmarked]))


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
    sum_unmarked, number = play_bingo(boards, numbers)
    print(sum_unmarked * number)


if __name__ == "__main__":
    main()
