import unittest
from scripts.helpers import loadInput
from scripts.year_2022.day_10.part_1.sol import solution as sol1
from scripts.year_2022.day_10.part_2.sol import solution as sol2

tests_1 = [
    ("scripts/year_2022/day_10/part_1/tinput.txt", 13140)
]

tests_2 = [
        ("scripts/year_2022/day_10/part_1/tinput.txt", "##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######.....")
]

class TestSolution(unittest.TestCase):
    def test_day_10_1(self): 
        for testCase in tests_1:
            testInput = loadInput(testCase[0])
            self.assertEqual(sol1(testInput), testCase[1])
    
    def test_day_10_2(self): 
        for testCase in tests_2:
            testInput = loadInput(testCase[0])
            self.assertEqual(sol2(testInput), testCase[1])
        
if __name__ == "__main__":
    unittest.main()