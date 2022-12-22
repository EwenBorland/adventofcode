import unittest
from scripts.year_2022.day_17.part_1.sol import solution as sol1
from scripts.year_2022.day_17.part_2.sol import solution as sol2

tests_1 = [
    ([
        "498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    ], 24),
]

tests_2 = [
    ([
        "498,4 -> 498,6 -> 496,6",
        "503,4 -> 502,4 -> 502,9 -> 494,9"
    ], 93),
]


class TestSolution(unittest.TestCase):
    def test_day_17_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])

    def test_day_17_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()