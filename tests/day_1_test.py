import unittest
from scripts.year_2022.day_1.part_1.sol import solution as sol1
from scripts.year_2022.day_1.part_2.sol import solution as sol2

tests_1 = [
    ([1000,2000,3000,"",4000,"",5000,6000,"",7000,8000,9000,"",10000,""], 24000)
]

tests_2 = [
    ([1000,2000,3000,"",4000,"",5000,6000,"",7000,8000,9000,"",10000,""], 45000)
]

class TestSolution(unittest.TestCase):
    def test_day_1_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_1_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])

if __name__ == "__main__":
    unittest.main()