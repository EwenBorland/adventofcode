import unittest
from scripts.helpers import loadInput
from scripts.year_2022.day_12.part_1.sol import solution as sol1
from scripts.year_2022.day_12.part_2.sol import solution as sol2

tests_1 = [
    (["Sabqponm","abcryxxl","accszExk","acctuvwj","abdefghi"], 31),
    (["SabcdefghijklmnopqrstuvwxyE"], 26)
]

tests_2 = [
    (["Sabqponm","abcryxxl","accszExk","acctuvwj","abdefghi"], 29),
    (["SabcdefghijklmnopqrstuvwxyE"], 25)
]

class TestSolution(unittest.TestCase):
    def test_day_12_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_12_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()