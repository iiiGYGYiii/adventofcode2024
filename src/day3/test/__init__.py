import unittest

from os import path

from .. import Solution

CWD = path.dirname(path.realpath(__file__))


class TestDay3(unittest.TestCase):
    def test_part1(self):
        filepath = path.join(CWD, "test_input.txt")
        result = Solution(filepath).part1()
        expected = 161
        self.assertEqual(result, expected, f"Expected {expected} got {result} instead.")

    def test_part2(self):
        filepath = path.join(CWD, "test_input.txt")
        result = Solution(filepath).part2()
        expected = 48
        self.assertEqual(result, expected, f"Expected {expected} got {result} instead.")


if __name__ == "__main__":
    unittest.main()
