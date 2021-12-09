import numpy as np

from aoc21 import utils


def sum_risk_levels(heightmap: np.ndarray) -> int:
    to_visit = np.full(heightmap.shape, True)
    rows, cols = heightmap.shape
    lows = []
    for i in range(rows):
        for j in range(cols):
            point = heightmap[i, j]
            neighbors = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            if all(
                point < heightmap[x, y]
                for x, y in neighbors
                if can_visit(to_visit, (x, y))
            ):
                lows.append(point)
    return sum(p + 1 for p in lows)


def top_3_basin_sizes_multiplied(heightmap: np.ndarray) -> int:
    to_visit = heightmap != 9
    sizes = []
    while point := pick(to_visit):
        sizes.append(visit_basin(to_visit, point))
    p = 1
    for s in sorted(sizes, reverse=True)[:3]:
        p *= s
    return p


def pick(to_visit: np.ndarray) -> tuple[int, int] | None:
    rows, cols = np.where(to_visit)
    pairs = list(zip(rows, cols))
    return pairs[0] if pairs else None


def visit_basin(to_visit: np.ndarray, start: tuple[int, int]) -> int:
    size = 0
    queue = {start}
    while queue:
        x, y = queue.pop()
        size += 1
        to_visit[x, y] = False
        candidates = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        queue.update(p for p in candidates if can_visit(to_visit, p))
    return size


def can_visit(to_visit: np.ndarray, point: tuple[int, int]) -> bool:
    rows, cols = to_visit.shape
    x, y = point
    return 0 <= x < rows and 0 <= y < cols and to_visit[x, y]


def parse_input(lines: list[str]) -> np.ndarray:
    return np.array([[int(c) for c in line] for line in lines])


def main():
    heightmap = parse_input(utils.read_input_lines(__file__))
    print(sum_risk_levels(heightmap))
    print(top_3_basin_sizes_multiplied(heightmap))


if __name__ == "__main__":
    main()
