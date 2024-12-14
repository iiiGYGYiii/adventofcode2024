from dataclasses import dataclass
from typing import List

PagesToProduce = List[int]


@dataclass
class OrderRule:
    before: int
    after: int


@dataclass
class Day5Input:
    order_rules: List[OrderRule]
    pages_to_produce: List[PagesToProduce]
