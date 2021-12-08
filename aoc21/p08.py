from aoc21 import utils

Entry = tuple[list[str], list[str]]  # (10, 4)


def count_easy_digits(entries: list[Entry]) -> int:
    """Count "easy" digits on our displays: 1, 4, 7, or 8."""
    easy_digit_lengths = {2, 3, 4, 7}
    digits = [
        digit
        for patterns, output in entries
        for digit in output
        if len(digit) in easy_digit_lengths
    ]
    return len(digits)


def parse_input(lines: list[str]) -> list[Entry]:
    res = []
    for line in lines:
        items = line.split()
        res.append((items[:10], items[11:]))
    return res


def main():
    entries = parse_input(utils.read_input_lines(__file__))
    print(count_easy_digits(entries))


if __name__ == "__main__":
    main()
