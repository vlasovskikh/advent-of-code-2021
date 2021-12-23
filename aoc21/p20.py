import itertools
from dataclasses import dataclass
from typing import Iterator

from aoc21 import utils


Coords = tuple[int, int]


@dataclass
class Image:
    pixels: dict[Coords, bool]
    xs: Coords
    ys: Coords
    background: bool = False

    def enhance(self, algo: list[bool], steps: int) -> None:
        for step in range(steps):
            new_pixels: dict[Coords, bool] = {}
            self.resize(1)
            for coords in self:
                code = self.pixel_code(coords)
                new_pixels[coords] = algo[code]
            self.background = (
                algo[0b111_111_111] if self.background else algo[0b000_000_000]
            )
            self.pixels = new_pixels

    def pixel_code(self, coords: Coords) -> int:
        cx, cy = coords
        value = 0
        for y in range(cy - 1, cy + 2):
            for x in range(cx - 1, cx + 2):
                value = value << 1 | self[(x, y)]
        return value

    def count_light_pixels(self) -> int:
        values = (self[coords] for coords in self)
        return sum(1 for v in values if v)

    def __getitem__(self, item: Coords) -> bool:
        return self.pixels.get(item, self.background)

    def __iter__(self) -> Iterator[Coords]:
        return itertools.product(range(*self.xs), range(*self.ys))

    def resize(self, inc: int) -> None:
        x1, x2 = self.xs
        y1, y2 = self.ys
        self.xs = (x1 - inc, x2 + inc)
        self.ys = (y1 - inc, y2 + inc)

    def show_range(self, xs: Coords, ys: Coords) -> str:
        lines = []
        for y in range(*ys):
            lines.append("".join(bool_to_char(self[(x, y)]) for x in range(*xs)))
        return "\n".join(lines)

    def __str__(self) -> str:
        return self.show_range(self.xs, self.ys)


def parse_input(lines: list[str]) -> tuple[list[bool], Image]:
    algo_line, _, *image_lines = lines
    algo = [char_to_bool(c) for c in algo_line]
    pixels: dict[Coords, bool] = {}
    cols, rows = len(image_lines[0]), len(image_lines)
    for y, line in enumerate(image_lines):
        for x, c in enumerate(line):
            pixels[(x, y)] = char_to_bool(c)
    return algo, Image(pixels, (0, cols), (0, rows))


def bool_to_char(b: bool) -> str:
    return "#" if b else "."


def char_to_bool(c: str) -> bool:
    if c == ".":
        return False
    elif c == "#":
        return True
    else:
        raise ValueError(f"Cannot covert {c!r} to bool")


def main() -> None:
    algo, image = parse_input(utils.read_input_lines(__file__))
    image.enhance(algo, 2)
    print(image.count_light_pixels())
    image.enhance(algo, 48)
    print(image.count_light_pixels())


if __name__ == "__main__":
    main()
