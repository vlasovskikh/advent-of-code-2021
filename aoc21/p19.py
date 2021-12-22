import functools
import itertools
from collections import defaultdict
from typing import Iterable, TypeVar

import numpy as np

from aoc21 import utils


def count_beacons(scanners: list[np.ndarray]) -> tuple[int, int]:
    overlaps: dict[int, list[int]] = defaultdict(list)
    pair_transforms: dict[tuple[int, int], np.ndarray] = {}

    indexes = range(len(scanners))
    all_pairs = list(itertools.product(indexes, indexes))
    not_connected = set()
    for step, (i1, i2) in enumerate(all_pairs):
        if (i2, i1) in not_connected or i1 == i2:
            continue
        print(f"{step * 100 // len(all_pairs)}%", end="\r", flush=True)
        if (res := scanner_transform(scanners[i2], scanners[i1])) is not None:
            overlaps[i1].append(i2)
            pair_transforms[(i1, i2)] = res
        else:
            not_connected.add((i1, i2))

    print()

    for path in all_paths(overlaps, 0):
        if len(path) < 2:
            continue
        last = path[-1]
        if (0, last) in pair_transforms:
            continue
        t = np.eye(4, dtype=int)
        for i1, i2 in utils.sliding_window(path, 2):
            t = t @ pair_transforms[(i1, i2)]
        pair_transforms[(0, last)] = t

    beacons: set[tuple] = set()
    for i, scanner in enumerate(scanners):
        pair = 0, i
        if i == 0:
            translated = scanner
        else:
            translated = translate(pair_transforms[pair], scanner)
        beacons |= to_set_of_tuples(translated)

    coords = [np.array([0, 0, 0])]
    for i in range(1, len(scanners)):
        t = pair_transforms[(0, i)]
        coords.append(t[0:3, 3])
    distances = (np.sum(np.abs(a - b)) for a, b in itertools.product(coords, coords))
    return len(beacons), max(distances)


T = TypeVar("T")


def all_paths(tree: dict[T, list[T]], start: T) -> Iterable[list[T]]:
    queue: list[tuple[T, ...]] = [(start,)]
    seen: set[tuple[T, ...]] = set()
    while queue:
        path = queue.pop()
        if path in seen:
            continue
        seen.add(path)
        *rest, last = path
        if last in rest:
            continue
        if rest:
            yield list(path)
        for s in tree.get(last, []):
            new_path: tuple[T, ...] = *path, s
            queue.append(new_path)


def translate(augmented_t: np.ndarray, points: np.ndarray) -> np.ndarray:
    rows, cols = points.shape
    augmented_points = np.vstack((points.T, np.ones(rows, dtype=int)))
    return (augmented_t @ augmented_points).T[:, :-1]


def augment(t: np.ndarray, b: np.ndarray) -> np.ndarray:
    rows, cols = t.shape
    t_bottom = np.vstack((t, np.zeros(cols, dtype=int)))
    b_1 = np.hstack((b, [1]))
    return np.hstack((t_bottom, b_1.reshape((rows + 1, 1))))


def shifts(src: np.ndarray, dst: np.ndarray, min_overlapping: int) -> Iterable[int]:
    dst_set = set(dst)
    repeats = len(dst_set) != len(dst)
    dst_dict = (
        {k: len(list(v)) for k, v in itertools.groupby(np.sort(dst))} if repeats else {}
    )
    shifts = {d - s for s, d in itertools.product(src, dst)}
    for shift in shifts:
        if repeats:
            shifted = {
                k: len(list(v)) for k, v in itertools.groupby(np.sort(src + shift))
            }
            common = set(shifted) & set(dst_dict)
            overlapping = sum(shifted[k] for k in common)
        else:
            overlapping = len(set(src + shift) & dst_set)
        if overlapping >= min_overlapping:
            yield shift


def scanner_shift(src: np.ndarray, dst: np.ndarray) -> np.ndarray | None:
    xs = list(shifts(src[:, 0], dst[:, 0], 12))
    ys = list(shifts(src[:, 1], dst[:, 1], 12))
    zs = list(shifts(src[:, 2], dst[:, 2], 12))
    dst_set = to_set_of_tuples(dst)
    seen = set()
    for coords in itertools.product(xs, ys, zs):
        if coords in seen:
            continue
        seen.add(coords)
        shift = np.array(coords)
        overlapping = to_set_of_tuples(src + shift) & dst_set
        if len(overlapping) >= 12:
            return shift
    return None


def scanner_transform(src: np.ndarray, dst: np.ndarray) -> np.ndarray | None:
    for t in all_transformations():
        a = (t @ src.T).T
        if (shift := scanner_shift(a, dst)) is not None:
            return augment(t, shift)
    return None


@functools.lru_cache()
def all_transformations() -> list[np.ndarray]:
    z90 = np.array(
        [
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1],
        ]
    )
    y90 = np.array(
        [
            [0, 0, -1],
            [0, 1, 0],
            [1, 0, 0],
        ]
    )
    x90 = np.array(
        [
            [1, 0, 0],
            [0, 0, -1],
            [0, 1, 0],
        ]
    )
    orientations = [
        all_rotations(y90, x90),
        all_rotations(y90 @ y90, z90),
        all_rotations(y90 @ y90 @ y90, x90),
        all_rotations(y90 @ y90 @ y90 @ y90, z90),
        all_rotations(x90, y90),
        all_rotations(x90 @ x90 @ x90, y90),
    ]
    return [x for xs in orientations for x in xs]


def all_rotations(t: np.ndarray, r: np.ndarray) -> list[np.ndarray]:
    return [
        t,
        t @ r,
        t @ r @ r,
        t @ r @ r @ r,
    ]


def to_set_of_tuples(a: np.ndarray) -> set[tuple]:
    return {tuple(row) for row in a}


def parse_input(lines: list[str]) -> list[np.ndarray]:
    scanners: list[np.ndarray] = []
    beacons: list[np.ndarray] = []
    lines.append("")
    for line in lines:
        if line.startswith("---"):
            beacons = []
        elif line:
            beacons.append([int(x) for x in line.split(",")])
        elif beacons:
            scanners.append(np.array(beacons))
    return scanners


def main() -> None:
    scanners = parse_input(utils.read_input_lines(__file__))
    print(count_beacons(scanners))


if __name__ == "__main__":
    main()
