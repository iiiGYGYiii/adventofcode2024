from typing import List

from .custom_types import Day5Input, OrderRule, PagesToProduce


class InputProcessor:
    def __init__(self, filepath: str):
        self.input: Day5Input = self._process_input(filepath)

    def _process_input(self, filepath: str) -> Day5Input:
        buff_order_rules = ""
        buff_pages_to_produce = ""

        with open(filepath, "r+") as file:
            buff_str = file.read()
            buff_order_rules, buff_pages_to_produce = buff_str.split("\n\n")

        raw_order_rules = buff_order_rules.strip().split("\n")
        raw_pages_to_produce = buff_pages_to_produce.strip().split("\n")

        return Day5Input(
            order_rules=self._parse_order_rule(raw_order_rules),
            pages_to_produce=self._parse_pages_to_produce(raw_pages_to_produce),
        )

    def _parse_order_rule(self, raw_order_rules: List[str]) -> List[OrderRule]:
        order_rules: List[OrderRule] = []
        for order_rule in raw_order_rules:
            before, after = tuple(map(int, order_rule.split("|")))
            order_rules.append(OrderRule(
                before=before,
                after=after,
            ))
        return order_rules

    def _parse_pages_to_produce(self, raw_pages_to_produce: List[str]) -> List[PagesToProduce]:
        return list(map(
            lambda buff_str: list(map(
                int,
                buff_str.split(",")
            )),
            raw_pages_to_produce
        ))
