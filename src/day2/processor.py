from .custom_types import Day2Input


class InputProcessor:
    def __init__(self, filepath: str):
        self.input = self._process_input(filepath)

    def _process_input(self, filepath: str) -> Day2Input:
        matrix = list()
        with open(filepath, "r+") as file:
            for line in file.readlines():
                matrix.append(list(map(int, line.strip().split(" "))))

        return Day2Input(matrix=matrix)
