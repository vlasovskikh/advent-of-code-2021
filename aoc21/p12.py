from __future__ import annotations
from collections import defaultdict

from aoc21 import utils


class Path:
    sequence: list[str]
    next: str
    visited: set[str]
    visited_twice: bool
    can_visit_twice: bool

    def __init__(
        self, sequence: list[str], next: str, *, can_visit_twice: bool
    ) -> None:
        self.sequence = sequence
        self.next = next
        self.visited = set(sequence)
        lower = [s for s in sequence if s.islower()]
        self.can_visit_twice = can_visit_twice
        self.visited_twice = len(lower) != len(set(lower))

    def __add__(self, other: str) -> Path:
        return Path(
            self.sequence + [self.next], other, can_visit_twice=self.can_visit_twice
        )

    def __str__(self) -> str:
        return (
            f"Path({self.sequence!r}, {self.next}, "
            "can_visit_twice={self.can_visit_twice})"
        )

    @property
    def can_visit(self) -> bool:
        if self.next == "start":
            return False
        elif self.next.islower() and self.next in self.visited:
            return self.can_visit_twice and not self.visited_twice
        else:
            return True

    def as_tuple(self) -> tuple[str, ...]:
        return *self.sequence, self.next


def count_paths(caves: dict[str, set[str]], *, can_visit_twice: bool) -> int:
    paths: set[tuple[str, ...]] = set()
    queue: list[Path] = [
        Path(["start"], c, can_visit_twice=can_visit_twice) for c in caves["start"]
    ]
    while queue:
        path = queue.pop()
        if path.next == "end":
            paths.add(path.as_tuple())
        elif path.can_visit:
            queue.extend([path + c for c in caves[path.next]])
    return len(paths)


def parse_input(lines: list[str]) -> dict[str, set[str]]:
    res: dict[str, set[str]] = defaultdict(lambda: set())
    for line in lines:
        a, b = line.split("-")
        res[a].add(b)
        res[b].add(a)
    return res


def main():
    caves = parse_input(utils.read_input_lines(__file__))
    print(count_paths(caves, can_visit_twice=False))
    print(count_paths(caves, can_visit_twice=True))


if __name__ == "__main__":
    main()
