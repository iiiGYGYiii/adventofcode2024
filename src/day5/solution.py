from typing import Any, Dict, List

from .custom_types import PagesToProduce
from .processor import InputProcessor


class Solution(InputProcessor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master_dict = self.map_to_master_dict()

    def part1(self) -> int:
        result = 0
        valid_to_produce: List[PagesToProduce] = list(filter(
            self.is_valid_to_produce,
            self.input.pages_to_produce
        ))
        result += self.get_sum_of_mid_values(valid_to_produce)
        return result

    def part2(self) -> int:
        result = 0
        invalid_to_produce: List[PagesToProduce] = list(filter(
            lambda item: not self.is_valid_to_produce(item),
            self.input.pages_to_produce,
        ))
        valid_to_produce: List[PagesToProduce] = list(map(
            self.transform_to_produceable,
            invalid_to_produce
        ))
        result += self.get_sum_of_mid_values(valid_to_produce)
        return result

    def map_to_master_dict(self) -> Dict[int, Dict[int, Any]]:
        master_dict: Dict[int, Dict[int, Any]] = dict()
        for rule in self.input.order_rules:
            before_dict = master_dict.get(rule.before)
            after_dict = master_dict.get(rule.after)

            if not before_dict:
                before_dict = dict()
                master_dict[rule.before] = before_dict

            if not after_dict:
                after_dict = dict()
                master_dict[rule.after] = after_dict

            before_dict[rule.after] = after_dict
        return master_dict

    def get_sum_of_mid_values(self, pages_to_produce: List[PagesToProduce]) -> int:
        return sum([pages[len(pages) // 2] for pages in pages_to_produce])

    def is_valid_to_produce(self, pages_to_produce: PagesToProduce) -> bool:
        is_valid = True
        last_index = len(pages_to_produce) - 1
        for index in range(last_index, 0, -1):
            page = pages_to_produce[index]
            is_valid = not any(
                before_page in self.master_dict[page]
                for before_page in pages_to_produce[:index]
            )
            if not is_valid:
                break
        return is_valid

    def transform_to_produceable(self, invalid_to_produce: PagesToProduce) -> PagesToProduce:
        index = 0
        mutable_invalid_to_produce = invalid_to_produce.copy()
        mid_index = len(mutable_invalid_to_produce) // 2
        while index <= mid_index:
            value = mutable_invalid_to_produce[index]

            if value < 0:
                index += 1
                continue

            has_mutation = False
            buff = mutable_invalid_to_produce[index + 1:]
            tail: List[int] = mutable_invalid_to_produce[:index]

            for buff_index in range(len(buff)):
                buff_val = buff[buff_index]
                if buff_val < 0:
                    continue
                if value in self.master_dict[buff_val]:
                    tail.append(buff_val)
                    buff[buff_index] = 0

            buff = list(filter(lambda v: v != 0, buff))

            tail.append(-value)
            has_mutation = len(tail) > 1
            if not has_mutation:
                index += 1
                mutable_invalid_to_produce = tail + buff
            else:
                mutable_invalid_to_produce = tail + buff

        return list(map(abs, mutable_invalid_to_produce))
