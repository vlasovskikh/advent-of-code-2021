import numpy as np

from aoc21 import utils


def model_fish(fish: np.ndarray, days: int) -> np.ndarray:
    """Model the life of a school of fish for the specified amount of days."""
    fish = fish.copy()
    for _ in range(days):
        fish -= 1
        new = np.full(np.sum(fish < 0), 8)
        fish = np.concatenate((fish, new))
        fish[fish < 0] = 6
    return fish


def parse_input(lines: list[str]) -> np.ndarray:
    return np.array([int(s) for line in lines for s in line.split(",")])


def main():
    fish = parse_input(utils.read_input_lines(__file__))
    print(len(model_fish(fish, 80)))
    print(len(model_fish(fish, 256)))


if __name__ == "__main__":
    main()
