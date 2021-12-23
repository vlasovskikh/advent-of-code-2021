import itertools

from aoc21 import utils


def losing_score_by_rolls(p1: int, p2: int) -> int:
    positions = [p1, p2]
    scores = [0, 0]
    die100 = itertools.cycle(range(1, 101))
    players = itertools.cycle(range(len(positions)))
    n_rolls = 0
    for player in players:
        roll = list(itertools.islice(die100, 3))
        n_rolls += len(roll)
        p = (positions[player] + sum(roll)) % 10
        positions[player] = p if p != 0 else 10
        scores[player] += positions[player]
        if scores[player] >= 1000:
            loser = (player + 1) % 2
            return scores[loser] * n_rolls
    raise ValueError("No winner found")


def parse_input(lines: list[str]) -> tuple[int, int]:
    p1, p2 = [int(line.split()[-1]) for line in lines]
    return p1, p2


def main() -> None:
    p1, p2 = parse_input(utils.read_input_lines(__file__))
    print(losing_score_by_rolls(p1, p2))


if __name__ == "__main__":
    main()
