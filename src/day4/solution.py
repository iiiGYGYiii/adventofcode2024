from .custom_types import Coordinates
from .processor import InputProcessor

TO_MATCH_WORD = "XMAS"
TO_MATCH_LEN = len(TO_MATCH_WORD)


class Solution(InputProcessor):
    def part1(self) -> int:
        result = 0
        for x_coord in self.input.x_coord:
            result += sum([
                self.times_horizontally_matches(x_coord),
                self.times_diagonally_matches(x_coord),
                self.times_vertically_matches(x_coord),
            ])
        return result

    def part2(self) -> int:
        result = 0
        for a_coord in self.input.a_coord:
            result += 1 if self._is_xmas(a_coord) else 0
        return result

    def times_horizontally_matches(self, x_coord: Coordinates) -> int:
        times = 0
        if self._can_go_forward(x_coord[0]):
            buff_str = "".join(self.input.puzzle[x_coord[1]][x_coord[0]:x_coord[0] + 4])
            times += 1 if buff_str == TO_MATCH_WORD else 0
        if self._can_go_backward(x_coord[0] + 1):
            buff_x = x_coord[0] + 1
            buff_str = "".join(
                self.input.puzzle[x_coord[1]][buff_x-4:buff_x][::-1]
            )
            times += 1 if buff_str == TO_MATCH_WORD else 0
        return times

    def times_vertically_matches(self, x_coord: Coordinates) -> int:
        times = 0
        if self._can_go_down(x_coord[1]):
            buff_str = "".join(list(map(
                lambda row: row[x_coord[0]],
                self.input.puzzle
            ))[x_coord[1]:x_coord[1] + 4])
            times += 1 if buff_str == TO_MATCH_WORD else 0
        if self._can_go_up(x_coord[1]):
            buff_y = x_coord[1] + 1
            buff_str = "".join(list(map(
                lambda row: row[x_coord[0]],
                self.input.puzzle
            ))[buff_y-4:buff_y][::-1])
            times += 1 if buff_str == TO_MATCH_WORD else 0
        return times

    def times_diagonally_matches(self, x_coord: Coordinates) -> int:
        times = 0
        steps = range(4)
        x, y = x_coord

        if self._can_go_up_left(x, y):
            buff_str = ""
            for step in steps:
                buff_str += self.input.puzzle[y - step][x - step]
            buff_str = "".join(buff_str)
            times += 1 if buff_str == TO_MATCH_WORD else 0

        if self._can_go_down_right(x, y):
            buff_str = ""
            for step in steps:
                buff_str += self.input.puzzle[y + step][x + step]
            buff_str = "".join(buff_str)
            times += 1 if buff_str == TO_MATCH_WORD else 0

        if self._can_go_up_right(x, y):
            buff_str = ""
            for step in steps:
                buff_str += self.input.puzzle[y - step][x + step]
            times += 1 if buff_str == TO_MATCH_WORD else 0

        if self._can_go_down_left(x, y):
            buff_str = ""
            for step in steps:
                buff_str += self.input.puzzle[y + step][x - step]
            buff_str = "".join(buff_str)
            times += 1 if buff_str == TO_MATCH_WORD else 0

        return times

    def _can_go_forward(self, x: int, match_len=TO_MATCH_LEN) -> bool:
        return x + match_len <= self.input.n

    def _can_go_backward(self, x: int, match_len=TO_MATCH_LEN) -> bool:
        return x - match_len >= 0

    def _can_go_down(self, y: int, match_len=TO_MATCH_LEN) -> bool:
        return y + match_len <= self.input.m

    def _can_go_up(self, y: int, match_len=TO_MATCH_LEN) -> bool:
        return y + 1 - match_len >= 0

    def _can_go_up_right(self, x: int, y: int, match_len=TO_MATCH_LEN) -> bool:
        return self._can_go_forward(x, match_len) and self._can_go_up(y, match_len)

    def _can_go_up_left(self, x: int, y: int, match_len=TO_MATCH_LEN) -> bool:
        return self._can_go_backward(x + 1, match_len) and self._can_go_up(y, match_len)

    def _can_go_down_right(self, x: int, y: int, match_len=TO_MATCH_LEN) -> bool:
        return self._can_go_forward(x, match_len) and self._can_go_down(y, match_len)

    def _can_go_down_left(self, x: int, y: int, match_len=TO_MATCH_LEN) -> bool:
        return self._can_go_backward(x + 1, match_len) and self._can_go_down(y, match_len)

    def _can_go_diagonally(self, x: int, y: int, match_len=TO_MATCH_LEN) -> bool:
        return (self._can_go_up_left(x, y, match_len)
                and self._can_go_up_right(x, y, match_len)
                and self._can_go_down_left(x, y, match_len)
                and self._can_go_down_right(x, y, match_len))

    def _is_xmas(self, a_coord: Coordinates) -> bool:
        x, y = a_coord

        if not self._can_go_diagonally(x, y, 2):
            return False

        is_xmas = False

        first_m = [1, 1]
        px, py = first_m
        if self.input.puzzle[y + py][x + px] != "M":
            px, py = (-px, -py)
            if self.input.puzzle[y + py][x + px] != "M":
                return False

        second_m = [1, -1]
        qx, qy = second_m
        if self.input.puzzle[y + qy][x + qx] != "M":
            qx, qy = (-qx, -qy)
            if self.input.puzzle[y + qy][x + qx] != "M":
                return False

        is_xmas = self.input.puzzle[y - qy][x - qx] == self.input.puzzle[y - py][x - px] == "S"
        return is_xmas
