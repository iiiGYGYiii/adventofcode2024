import re
from typing import List

from .custom_types import Day4Input, Coordinates


class InputProcessor:
    def __init__(self, filepath: str):
        self.input: Day4Input = self._process_input(filepath)

    def _process_input(self, filepath: str) -> Day4Input:
        puzzle: List[List[str]] = []
        x_coord: List[Coordinates] = []
        a_coord: List[Coordinates] = []
        with open(filepath, "r+") as file:
            row_index = 0
            for line in file.readlines():
                puzzle.append(list(line.strip()))
                x_coord.extend([
                    (match.start(), row_index)
                    for match in re.finditer(r"X", line)
                ])
                a_coord.extend([
                    (match.start(), row_index)
                    for match in re.finditer(r"A", line)
                ])
                row_index += 1
        return Day4Input(
            puzzle=puzzle,
            x_coord=x_coord,
            a_coord=a_coord,
        )
