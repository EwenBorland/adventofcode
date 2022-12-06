import unittest
from scripts.year_2022.day_6.part_1.sol import solution as sol1
from scripts.year_2022.day_6.part_2.sol import solution as sol2

tests_1 = [
    (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 7),
    (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 5),
    (["nppdvjthqldpwncqszvftbrmjlhg"], 6),
    (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 10),
    (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 11)
]


tests_2 = [
    (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 19),
    (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 23),
    (["nppdvjthqldpwncqszvftbrmjlhg"], 23),
    (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 29),
    (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26)
]

class TestSolution(unittest.TestCase):
    def test_day_6_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_6_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()