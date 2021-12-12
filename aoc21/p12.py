from collections import defaultdict

from aoc21 import utils


def count_paths(caves: dict[str, set[str]]) -> int:
    paths: set[tuple[str, ...]] = set()
    queue: list[tuple[str, ...]] = [("start", c) for c in caves["start"]]
    while queue:
        path = queue.pop()
        *rest, last = path
        if last == "end":
            paths.add(path)
        elif last.islower() and last in rest:  # O(N)
            pass
        else:
            queue.extend([(*path, c) for c in caves[last]])
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
    print(count_paths(caves))


if __name__ == "__main__":
    main()
