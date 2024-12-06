import unittest

from os import path

from .. import Solution

CWD = path.dirname(path.realpath(__file__))


class TestDay2(unittest.TestCase):
    def test_part1(self):
        filepath = path.join(CWD, "test_input.txt")
        result = Solution(filepath).part1()
        expected = 2
        self.assertEqual(result, expected, f"Expected {expected} got {result} instead.")

    def test_part2(self):
        pass
        filepath = path.join(CWD, "test_input.txt")
        result = Solution(filepath).part2()
        expected = 4
        self.assertEqual(result, expected, f"Expected {expected} got {result} instead.")

if __name__ == "__main__":
    unittest.main()
