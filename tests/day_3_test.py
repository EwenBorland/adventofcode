import unittest
from scripts.year_2022.day_3.part_1.sol import solution as sol1
from scripts.year_2022.day_3.part_2.sol import solution as sol2

tests_1 = [
    (["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"], 157)
]

tests_2 = [
    (["vJrwpWtwJgWrhcsFMMfFFhFp\n", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n", "PmmdzqPrVvPwwTWBwg\n", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n", "ttgJtRGJQctTZtZT\n", "CrZsJsPPZsGzwwsLwLmpwMDw\n"], 70)
]

class TestSolution(unittest.TestCase):
    def test_day_3_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_2_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])

if __name__ == "__main__":
    unittest.main()