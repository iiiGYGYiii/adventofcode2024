from .custom_types import Day1Input


class InputProcessor:
    def __init__(self, filepath: str):
        self.input = self._process_input(filepath)

    def _process_input(self, filepath: str) -> Day1Input:
        left_list = list()
        right_list = list()
        with open(filepath, "r+") as file:
            for line in file.readlines():
                line = line.strip().split("   ")
                left_val, right_val = [int(v) for v in line]
                left_list.append(left_val)
                right_list.append(right_val)
        return Day1Input(left_list=left_list, right_list=right_list)
