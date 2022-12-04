import unittest
from scripts.year_2022.day_4.part_1.sol import solution as sol1, compare_pair
from scripts.year_2022.day_4.part_2.sol import solution as sol2, compare_pair_outside

tests_1 = [
    (["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8"], 2)
]

tests_compare = [
    ("12-86,4-77", False),
    ("2-4,6-8", False),
    ("2-3,4-5",False),
    ("5-7,7-9",False),
    ("2-8,3-7",True),
    ("6-6,4-6",True),
    ("2-6,4-8",False)
]

tests_2 = [
    (["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8"], 4)
]

class TestSolution(unittest.TestCase):
    def test_day_4_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_4_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
    def test_compare(self):
        for testCase in tests_compare:
            self.assertEqual(compare_pair(testCase[0],testCase[1]), testCase[1])
if __name__ == "__main__":
    unittest.main()