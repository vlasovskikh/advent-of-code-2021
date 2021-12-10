from aoc21.p10 import (
    check_syntax,
    syntax_error_score,
    autocomplete,
    autocomplete_lines_score,
    autocomplete_lines,
)


def test_example():
    lines = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip().splitlines()
    lines = [line.strip() for line in lines]
    assert syntax_error_score(check_syntax(lines)) == 26397
    assert autocomplete_lines_score(autocomplete_lines(lines)) == 288957


def test_autocomplete_1():
    assert autocomplete("[({(<(())[]>[[{[]{<()<>>") == "}}]])})]"
