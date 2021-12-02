from dataclasses import dataclass

from aoc21 import utils


@dataclass
class Submarine:
    """Submarine that executes movement commands and keeps track of its coordinates."""

    use_aim: bool
    x: int = 0
    y: int = 0
    aim: int = 0

    def forward(self, x: int) -> None:
        """Go forward `x` units and, possibly, change depth if the object uses
        depth aiming."""
        self.x += x
        if self.use_aim:
            self.y += x * self.aim

    def down(self, arg: int) -> None:
        """Go down `arg` units, or increase depth aim."""
        if self.use_aim:
            self.aim += arg
        else:
            self.y += arg

    def up(self, arg: int) -> None:
        """Go up `arg` units, or decrease depth aim."""
        if self.use_aim:
            self.aim -= arg
        else:
            self.y -= arg


def execute_submarine_commands(
    commands: list[tuple[str, int]],
    *,
    use_aim: bool,
) -> tuple[int, int]:
    """Execute the log of submarine commands and return its (horizontal position,
    depth).

    Set `use_aim` to `True` to use the aim semantics from the Part 2.
    """
    submarine = Submarine(use_aim=use_aim)
    for cmd, arg in commands:
        f = getattr(submarine, cmd)
        f(arg)
    return submarine.x, submarine.y


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
