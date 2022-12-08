import unittest
from scripts.year_2022.day_8.part_1.sol import solution as sol1
from scripts.year_2022.day_8.part_2.sol import solution as sol2

tests_1 = [
    ([
        "30373",
        "25512",
        "65332",
        "33549",
        "35390"
        ],
        21),
    ([
        "1"
        ],1),
    ([
        "11",
        "11"
        ],4),
    ([
        "13",
        "31"
        ],4),
    ([
        "31",
        "13"
        ],4),
    ([
        "111",
        "111",
        "111"
        ],8),
    ([
        "111",
        "121",
        "111"
        ],9),
    ([
        "121",
        "222",
        "121"
        ],8),
    ([
        "222",
        "222",
        "222"
        ],8),
    ([
        "222",
        "212",
        "222"
        ],8),
    ([
        "1111",
        "1111",
        "1111"
        ],10),
    ([
        "1111",
        "1121",
        "1111"
        ],11),
    ([
        "1211",
        "2121",
        "1211"
        ],11),
    ([
        "1211",
        "2221",
        "1211"
        ],11),
    ([
        "1211",
        "2211",
        "1211"
        ],11),
]

tests_2 = [
    (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 19),
    (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 23),
    (["nppdvjthqldpwncqszvftbrmjlhg"], 23),
    (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 29),
    (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26)
]

class TestSolution(unittest.TestCase):
    def test_day_8_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_8_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()