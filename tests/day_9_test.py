import unittest
from scripts.year_2022.day_9.part_1.sol import solution as sol1
from scripts.year_2022.day_9.part_2.sol import solution as sol2

tests_1 = [
    ([
        "R 4",
        "U 4",
        "L 3",
        "R 4",
        "D 1",
        "L 5",
        "R 2 "
        ],
        13),
   
]

tests_2 = [
    ([
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
        ],
        8),
]

class TestSolution(unittest.TestCase):
    def test_day_9_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_9_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()