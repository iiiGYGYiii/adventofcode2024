from .processor import InputProcessor


class Solution(InputProcessor):
    def part1(self) -> int:
        result = 0
        for operation in self.input.operations:
            result += operation.values[0] * operation.values[1]
        return result

    def part2(self) -> int:
        result = 0
        for operation in self.input.operations:
            if not operation.is_ignored(self.input.ignore_ranges):
                result += operation.values[0] * operation.values[1]
        return result


# TO BE SUBMITTED IN ZTM ILL PROVIDE THE INPUT PROCESSOR HERE
# AS HOW THE INPUT WAS PROCESSED IS CRUCIAL

# import re
# from typing import List
#
# from .custom_types import Operation, Operations, Day3Input, IgnoreRange
#
# MUL_REGEX = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
# INSTRUCTIONS_REGEX = re.compile(r"(don't\(\)|do\(\))")
#
# DONT_LITERAL = "don't()"
# DO_LITERAL = "do()"
#
#
# class InputProcessor:
#     def __init__(self, filepath: str):
#         self.input = self._process_input(filepath)
#
#     def _process_input(self, filepath: str) -> Day3Input:
#         operations: Operations = []
#         instructions = []
#         ignore_ranges: List[IgnoreRange] = []
#         with open(filepath, "r+") as file:
#             index = 0
#
#             for line in file.readlines():
#                 instructions.extend([
#                     dict(
#                         start=match.start() + index,
#                         text=match.group()
#                     ) for match in re.finditer(
#                         INSTRUCTIONS_REGEX, line)
#                 ])
#
#                 operations.extend([
#                     Operation(
#                         values=(
#                             int(match.group()[4:-1].split(",")[0]),
#                             int(match.group()[4:-1].split(",")[1]),
#                         ),
#                         index=index + match.start()
#                     )
#                     for match in re.finditer(MUL_REGEX, line)
#                 ])
#
#                 index += len(line)
#
#         ignore_range = IgnoreRange()
#
#         for instruction in instructions:
#             if instruction["text"] == DONT_LITERAL:
#                 if not ignore_range.is_open():
#                     ignore_range.dont_index = instruction["start"]
#
#             if instruction["text"] == DO_LITERAL:
#                 if ignore_range.is_open():
#                     ignore_range.do_index = instruction["start"]
#                     ignore_ranges.append(ignore_range)
#                     ignore_range = IgnoreRange()
#
#         return Day3Input(
#             operations=operations,
#             ignore_ranges=ignore_ranges
#         )
