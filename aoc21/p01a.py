from aoc21 import utils


def count_depth_increases(measurements: list[int]) -> int:
    """Count the number of times a depth measurement increases from the previous
    measurement.
    """
    if not measurements:
        return 0
    shifted = iter(measurements)
    next(shifted)
    pairs = zip(measurements, shifted)
    increases = (1 for x, y in pairs if x < y)
    return sum(increases)


def parse_input(lines: list[str]) -> list[int]:
    return [int(line) for line in lines]


if __name__ == "__main__":
    data = parse_input(utils.read_input_lines(__file__))
    print(count_depth_increases(data))
