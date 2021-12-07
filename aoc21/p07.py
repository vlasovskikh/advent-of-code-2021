from aoc21 import utils


def minimize_fuel(crabs: list[int], *, expensive_fuel: bool) -> int:
    fuels = []
    for p in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            diff = abs(crab - p)
            if expensive_fuel:
                half = diff // 2
                s = (diff + 1) * half
                if diff % 2 == 1:
                    s += half + 1
            else:
                s = diff
            fuel += s
        fuels.append(fuel)
    return min(fuels)


def parse_input(lines: list[str]) -> list[int]:
    return [int(s) for line in lines for s in line.split(",")]


def main():
    crabs = parse_input(utils.read_input_lines(__file__))
    print(minimize_fuel(crabs, expensive_fuel=False))
    print(minimize_fuel(crabs, expensive_fuel=True))


if __name__ == "__main__":
    main()
