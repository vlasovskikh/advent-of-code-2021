from collections import defaultdict

from funcparserlib.parser import a, many, forward_decl, NoParseError, finished


from aoc21 import utils


def check_syntax(lines: list[str]) -> dict[str, int]:
    chunk = forward_decl()
    chunks = many(chunk)
    parens = -a("(") + chunks + -a(")")
    squares = -a("[") + chunks + -a("]")
    curlies = -a("{") + chunks + -a("}")
    angles = -a("<") + chunks + -a(">")
    chunk.define(parens | squares | curlies | angles)
    tree = chunks + -finished

    errors: dict[str, int] = defaultdict(lambda: 0)

    for line in lines:
        try:
            tree.parse(line)
        except NoParseError as e:
            error_pos = e.state.max
            if error_pos < len(line):
                errors[line[error_pos]] += 1

    return errors


def syntax_error_score(errors: dict[str, int]) -> int:
    scoring = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    return sum(scoring[k] * v for k, v in errors.items())


def main():
    lines = utils.read_input_lines(__file__)
    print(syntax_error_score(check_syntax(lines)))


if __name__ == "__main__":
    main()
