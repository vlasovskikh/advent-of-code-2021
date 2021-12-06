import itertools

from aoc21 import utils


def model_fish(fish: list[int], days: int) -> int:
    """Model the life of a school of fish for the specified amount of days."""
    counts = compress_fish(fish)
    for _ in range(days):
        # i:  0 1 2 3 4 5 6 7 8 9
        # s: -1 0 1 2 3 4 5 6 7 8
        counts.pop(state(-1))
        new = counts[state(-1)]
        counts.append(new)
        counts[state(6)] += new
    return sum(counts[1:])


def state(s: int) -> int:
    """Get the index of compressed fish from the living state of fish."""
    return s + 1


def compress_fish(fish: list[int]) -> list[int]:
    """Returns an array of fish count in each of the fish states: [-1, 0..8].

    * -1 — the state of creating a new fish
    * 0..8 — the amount of days before creating a new fish
    """
    grouped = {k: len(list(g)) for k, g in itertools.groupby(sorted(fish))}
    return [grouped.get(i, 0) for i in range(-1, 9)]


def parse_input(lines: list[str]) -> list[int]:
    return [int(s) for line in lines for s in line.split(",")]


def main():
    fish = parse_input(utils.read_input_lines(__file__))
    print(model_fish(fish, 80))
    print(model_fish(fish, 256))


if __name__ == "__main__":
    main()
