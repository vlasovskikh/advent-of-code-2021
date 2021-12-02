from aoc21 import utils


def execute_submarine_commands(
    commands: list[tuple[str, int]],
    *,
    use_aim: bool,
) -> tuple[int, int]:
    """Execute the log of submarine commands and return its (horizontal position,
    depth).

    Set `use_aim` to `True` to use the aim semantics from the Part 2.
    """
    x, y, aim = 0, 0, 0
    for cmd, arg in commands:
        if cmd == "forward":
            x += arg
            if use_aim:
                y += arg * aim
        elif cmd == "down":
            if use_aim:
                aim += arg
            else:
                y += arg
        elif cmd == "up":
            if use_aim:
                aim -= arg
            else:
                y -= arg
        else:
            raise ValueError(f"Unknown command: '{cmd} {arg}'")
    return x, y


def parse_input(lines: list[str]) -> list[tuple[str, int]]:
    splits = (line.split() for line in lines)
    return [(cmd, int(arg)) for cmd, arg in splits]


def main():
    data = parse_input(utils.read_input_lines(__file__))
    for use_aim in [False, True]:
        x, y = execute_submarine_commands(data, use_aim=use_aim)
        print(x * y)


if __name__ == "__main__":
    main()
