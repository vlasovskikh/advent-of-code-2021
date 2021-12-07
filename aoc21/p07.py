from aoc21 import utils


def minimize_fuel(crabs: list[int]) -> int:
    fuels = []
    for p in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - p)
        fuels.append(fuel)
    return min(fuels)


def parse_input(lines: list[str]) -> list[int]:
    return [int(s) for line in lines for s in line.split(",")]


def main():
    crabs = parse_input(utils.read_input_lines(__file__))
    print(minimize_fuel(crabs))


if __name__ == "__main__":
    main()
