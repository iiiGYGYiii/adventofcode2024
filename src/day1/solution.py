from collections import Counter

from .processor import InputProcessor


class Solution(InputProcessor):
    def part1(self) -> int:
        right_list = self.input.right_list.copy()
        left_list = self.input.left_list.copy()

        right_list.sort()
        left_list.sort()

        result = 0

        for index in range(len(left_list)):
            result += abs(right_list[index] - left_list[index])

        return result

    def part2(self) -> int:
        result = 0
        right_counter = Counter(self.input.right_list)
        left_counter = Counter(self.input.left_list)

        for number, counter in left_counter.items():
            if not right_counter[number]:
                continue

            result += number * right_counter[number] * left_counter[number]

        return result
