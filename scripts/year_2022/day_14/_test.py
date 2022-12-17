import unittest
from scripts.year_2022.day_14.part_1.sol import solution as sol1, calculateLine
from scripts.year_2022.day_14.part_2.sol import solution as sol2

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
tests_calcLine = [
    ([0,0], [0,2], [[0,0],[0,1],[0,2]]),
]

class TestSolution(unittest.TestCase):
    def test_day_14_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])

    def test_day_14_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])

    def test_calculateLine(self):
        for testCase in tests_calcLine:
            self.assertEqual(calculateLine(testCase[0],testCase[1]),testCase[2])
        
if __name__ == "__main__":
    unittest.main()