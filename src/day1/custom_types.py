from dataclasses import dataclass, field
from typing import List

@dataclass
class Day1Input:
    right_list: List[int] = field(default_factory=list)
    left_list: List[int] = field(default_factory=list)
