from aoc21 import utils


def gamma_and_epsilon(report: list[str]) -> tuple[int, int]:
    """Calculates gamma and epsilon for a submarine diagnostic report."""
    if not report:
        return 0, 0
    bits = len(report[0])
    half = len(report) / 2
    counters = [0] * bits
    for line in report:
        for i, c in enumerate(line):
            if c == "1":
                counters[i] += 1
    for i, counter in enumerate(counters):
        if counter == half:
            raise ValueError(f"Same amount of zeros and ones in column {i}: {counter}")
    g_bits = [c > half for c in counters]
    e_bits = [not bit for bit in g_bits]
    return bools_to_int(g_bits), bools_to_int(e_bits)


def bools_to_int(xs: list[bool]) -> int:
    """Convert a boolean list into the corresponding integer using base 2."""
    return int("".join("1" if x else "0" for x in xs), base=2)


if __name__ == "__main__":
    lines = utils.read_input_lines(__file__)
    g, e = gamma_and_epsilon(lines)
    print(g * e)
