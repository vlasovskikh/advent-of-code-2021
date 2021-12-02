from aoc21 import utils


def execute_submarine_commands(commands: list[tuple[str, int]]) -> tuple[int, int]:
    """Execute the log of submarine commands and return its (horizontal position,
    depth)."""
    x, y = 0, 0
    for cmd, arg in commands:
        if cmd == "forward":
            x += arg
        elif cmd == "down":
            y += arg
        elif cmd == "up":
            y -= arg
        else:
            raise ValueError(f"Unknown command: '{cmd} {arg}'")
    return x, y


def parse_input(lines: list[str]) -> list[tuple[str, int]]:
    splits = (line.split() for line in lines)
    return [(cmd, int(arg)) for cmd, arg in splits]


def main():
    data = parse_input(utils.read_input_lines(__file__))
    x, y = execute_submarine_commands(data)
    print(x * y)


if __name__ == "__main__":
    main()
