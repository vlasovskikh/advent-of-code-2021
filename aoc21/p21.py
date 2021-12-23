from __future__ import annotations
import itertools
from collections import defaultdict, Counter
from typing import NamedTuple

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


class Universe(NamedTuple):
    positions: tuple[int, int]
    scores: tuple[int, int]
    player: int

    def transform(self, roll: int) -> Universe:
        p = (self.positions[self.player] + roll) % 10
        if p == 0:
            p = 10
        s = self.scores[self.player] + p
        p1, p2 = self.positions
        positions = (p, p2) if self.player == 0 else (p1, p)
        s1, s2 = self.scores
        scores = (s, s2) if self.player == 0 else (s1, s)
        return Universe(positions, scores, (self.player + 1) % 2)


def max_winning_universes(p1: int, p2: int) -> int:
    universes: dict[Universe, int] = defaultdict(int)
    universes[Universe((p1, p2), (0, 0), 0)] = 1
    wins = [0, 0]
    winning_score = 21
    rolls: dict[int, int] = Counter(
        sum(roll) for roll in itertools.product(range(1, 4), range(1, 4), range(1, 4))
    )
    while universes:
        to_remove: set[Universe] = set()
        to_update: dict[Universe, int] = defaultdict(int)
        for universe, count in universes.items():
            s1, s2 = universe.scores
            if s1 >= winning_score or s2 >= winning_score:
                winner = 0 if s1 > s2 else 1
                to_remove.add(universe)
                wins[winner] += count
                continue
            for roll, n in rolls.items():
                to_update[universe.transform(roll)] += count * n
            to_update[universe] -= count
        for universe, count in to_update.items():
            universes[universe] += count
            if universes[universe] == 0:
                to_remove.add(universe)
        for universe in to_remove:
            del universes[universe]
    return max(wins)


def parse_input(lines: list[str]) -> tuple[int, int]:
    p1, p2 = [int(line.split()[-1]) for line in lines]
    return p1, p2


def main() -> None:
    p1, p2 = parse_input(utils.read_input_lines(__file__))
    print(losing_score_by_rolls(p1, p2))
    print(max_winning_universes(p1, p2))


if __name__ == "__main__":
    main()
