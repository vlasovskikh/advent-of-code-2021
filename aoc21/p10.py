from collections import defaultdict

from funcparserlib.parser import (
    a,
    many,
    forward_decl,
    NoParseError,
    finished,
    Parser,
    maybe,
)

from aoc21 import utils


def valid_chunks_parser() -> Parser:
    chunk = forward_decl()
    chunks = many(chunk)
    parens = -a("(") + chunks + -a(")")
    squares = -a("[") + chunks + -a("]")
    curlies = -a("{") + chunks + -a("}")
    angles = -a("<") + chunks + -a(">")
    chunk.define(parens | squares | curlies | angles)
    return chunks + -finished


def incomplete_chunks_parser() -> Parser:
    chunk = forward_decl()
    chunks = many(chunk)
    parens = a("(") + chunks + maybe(a(")"))
    squares = a("[") + chunks + maybe(a("]"))
    curlies = a("{") + chunks + maybe(a("}"))
    angles = a("<") + chunks + maybe(a(">"))
    chunk.define(parens | squares | curlies | angles)
    return chunks + -finished


def corrupted_char(line: str) -> str | None:
    try:
        valid_chunks_parser().parse(line)
    except NoParseError as e:
        error_pos = e.state.max
        if error_pos < len(line):
            return line[error_pos]
    return None


def check_syntax(lines: list[str]) -> dict[str, int]:
    errors: dict[str, int] = defaultdict(lambda: 0)
    for line in lines:
        if c := corrupted_char(line):
            errors[c] += 1
    return errors


def autocomplete_lines(lines: list[str]) -> list[str]:
    return [autocomplete(line) for line in lines if not corrupted_char(line)]


def autocomplete(line: str) -> str:
    chunks = incomplete_chunks_parser().parse(line)
    return closing_brackets(chunks)


def closing_brackets(chunks: list) -> str:
    closing = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    if not chunks:
        return ""
    start, children, stop = chunks[-1]
    c = "" if stop else closing[start]
    return closing_brackets(children) + c


def syntax_error_score(errors: dict[str, int]) -> int:
    scoring = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return sum(scoring[k] * v for k, v in errors.items())


def autocomplete_score(completion: str) -> int:
    scoring = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    s = 0
    for c in completion:
        s = s * 5 + scoring[c]
    return s


def autocomplete_lines_score(completions: list[str]) -> int:
    winners = list(sorted(autocomplete_score(c) for c in completions))
    assert len(winners) % 2 == 1
    return winners[len(winners) // 2]


def main():
    lines = utils.read_input_lines(__file__)
    print(syntax_error_score(check_syntax(lines)))
    print(autocomplete_lines_score(autocomplete_lines(lines)))


if __name__ == "__main__":
    main()
