from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class IgnoreRange:
    dont_index: int = -1
    do_index: int = -1

    def is_open(self):
        return self.dont_index != -1 and self.do_index == -1


@dataclass
class Operation:
    values: Tuple[int, int]
    index: int

    def is_ignored(self, ignore_ranges: List[IgnoreRange]):
        return any(range.dont_index <= self.index <= range.do_index for range in ignore_ranges)


Operations = List[Operation]


@dataclass
class Day3Input:
    operations: Operations
    ignore_ranges: List[IgnoreRange]
