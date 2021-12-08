import itertools

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


def sum_of_decoded_values(entries: list[Entry]) -> int:
    """Sum all the values in entries decoded in accordance to their patterns."""
    return sum(decode_value(patterns, output) for patterns, output in entries)


def decode_value(patterns: list[str], output: list[str]) -> int:
    s = "abcdefg"  # noqa
    # noinspection SpellCheckingInspection
    digits = [
        "abcefg",
        "cf",
        "acdeg",
        "acdfg",
        "bcdf",
        "abdfg",
        "abdefg",
        "acf",
        "abcdefg",
        "abcdfg",
    ]
    digit_set = set(digits)
    for permutation in itertools.permutations(s):
        table = str.maketrans(dict(zip(permutation, s)))
        decoded = (decode_digit(p, table) for p in patterns)
        if all(d in digit_set for d in decoded):
            numbers = [digits.index(decode_digit(d, table)) for d in output]
            return int("".join(str(n) for n in numbers))
    raise ValueError("Decode key not found")


def decode_digit(pattern: str, table: dict[int, str]) -> str:
    """The decoded digit for the pattern using the translation table."""
    return "".join(sorted(pattern.translate(table)))


def parse_input(lines: list[str]) -> list[Entry]:
    res = []
    for line in lines:
        items = line.split()
        res.append((items[:10], items[11:]))
    return res


def main():
    entries = parse_input(utils.read_input_lines(__file__))
    print(count_easy_digits(entries))
    print(sum_of_decoded_values(entries))


if __name__ == "__main__":
    main()
