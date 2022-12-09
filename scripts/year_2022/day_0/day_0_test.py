import unittest
from scripts.year_2022.day_0.part_1.sol import solution as sol1
from scripts.year_2022.day_0.part_2.sol import solution as sol2

tests_1 = [
    ([199,200,208,210,200,207,240,269,260,263], 7),
    ([199,200,208,210,200,207,240,269,260,263,264], 8)
]

tests_2 = [
    ([199,200,208,210,200,207,240,269,260,263], 5)
]

class TestSolution(unittest.TestCase):
    def test_day_0_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_0_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])

if __name__ == "__main__":
    unittest.main()