import os
from pathlib import Path


def read_input_lines(module_path: str) -> list[str]:
    """Read lines of the input file that corresponds to the module name."""
    with open(input_file_path(module_path), "r") as fd:
        return [s.strip() for s in fd.readlines()]


def input_file_path(module_path: str) -> Path:
    """Input file path from `data/` that corresponds to the module name."""
    p = Path(module_path)  # "/Users/vlan/exp/2021/aoc21/p01a.py"
    module_name, _ = os.path.splitext(p.name)
    return p.parent / ".." / "data" / f"{module_name}.txt"
