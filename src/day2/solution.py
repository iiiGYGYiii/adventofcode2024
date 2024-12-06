from typing import List, Literal, Tuple

from .processor import InputProcessor

MAX_GAP = 3
SLOPE = Literal[-1, 0, 1]

IDK = dict(
    increase=1,
    decrease=-1,
    null=0,
)


class Solution(InputProcessor):
    def part1(self) -> int:
        result = 0
        for row in self.input.matrix:
            if self.is_safe(row):
                result += 1
        return result

    def part2(self) -> int:
        result = 0
        for row in self.input.matrix:
            if self.is_safe(row, allow_failure=True):
                result += 1
        return result

    @staticmethod
    def is_safe(row: List[int], allow_failure=False) -> bool:
        is_safe = True
        to_index = len(row) - 1
        slope = Solution.get_slope(row[0], row[1])
        skip_index = -1
        is_sliced = False
        for index in range(to_index):
            if index == skip_index:
                continue
            current_value = row[index]
            next_value = row[index + 1]
            is_safe = is_safe and Solution.is_val_safe(current_value, next_value, slope)
            if not is_safe:
                if not allow_failure or is_sliced:
                    break
                is_safe, skip_index, slope = Solution.can_be_safe(row, index, slope)
                if not is_safe:
                    break
                is_sliced = True
        return is_safe

    @staticmethod
    def get_slope(prev_value: int, current_value: int) -> SLOPE:
        if prev_value == current_value or abs(prev_value - current_value) > MAX_GAP:
            return 0
        return -1 if current_value < prev_value else 1

    @staticmethod
    def is_val_safe(prev_value: int, current_val: int, slope: SLOPE) -> bool:
        return Solution.get_slope(prev_value, current_val) * slope > 0

    @staticmethod
    def can_be_safe(row: List[int], failed_at: int, slope: SLOPE) -> Tuple[bool, int, SLOPE]:
        is_safe = True
        new_slope = slope
        skip_index = failed_at
        if failed_at == 0:
            new_slope = Solution.get_slope(row[2], row[3])
            if Solution.is_val_safe(row[0], row[2], new_slope):
                skip_index = 1
            elif Solution.is_val_safe(row[1], row[2], new_slope):
                skip_index = 0
            else:
                is_safe = False
        elif failed_at == 1:
            prob_new_slope = Solution.get_slope(row[2], row[3])
            if Solution.is_val_safe(row[0], row[2], prob_new_slope):
                new_slope = prob_new_slope
            elif Solution.is_val_safe(row[1], row[3], slope):
                skip_index = failed_at + 1
            elif Solution.is_val_safe(row[1], row[2], prob_new_slope):
                skip_index = 0
                new_slope = prob_new_slope
            else:
                is_safe = False
        elif failed_at == len(row) - 2:
            pass
        else:
            discard_next = Solution.is_val_safe(row[failed_at], row[failed_at + 2], slope)
            if discard_next:
                is_safe = True
                skip_index = failed_at + 1
            else:
                is_safe = Solution.is_val_safe(row[failed_at - 1], row[failed_at + 1], slope)
                skip_index = failed_at

        return is_safe, skip_index, new_slope
