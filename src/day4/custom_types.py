from dataclasses import dataclass, field
from typing import List, Tuple

Coordinates = Tuple[int, int]


@dataclass
class Day4Input:
    puzzle: List[List[str]]
    x_coord: List[Coordinates]
    a_coord: List[Coordinates]
    m: int = field(init=False)
    n: int = field(init=False)

    def __post_init__(self):
        self.m = len(self.puzzle)
        self.n = len(self.puzzle[0])
