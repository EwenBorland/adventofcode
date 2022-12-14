import unittest
from scripts.helpers import loadInput
from scripts.year_2022.day_13.part_1.sol import solution as sol1, compareLR
from scripts.year_2022.day_13.part_2.sol import solution as sol2

tests_1 = [
    ([
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
        ""
    ], 13),
]

tests_compareLR = [
    ([[1,1,3,1,1],[1,1,5,1,1]],(True,True)),
    ([[[1],[2,3,4]],[[1],4]],(True,True)),
    ([[9],[[8,7,6]]],(False,True)),
    ([[[4,4],4,4],[[4,4],4,4,4]],(True,True)),
    ([[7,7,7,7],[7,7,7]],(False,True)),
    ([[],[3]],(True,True)),
    ([[[[]]],[[]]],(False,True)),
    ([[1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]],(False,True)),
    ]

tests_2 = [
    ([
        "[1,1,3,1,1]",
        "[1,1,5,1,1]",
        "",
        "[[1],[2,3,4]]",
        "[[1],4]",
        "",
        "[9]",
        "[[8,7,6]]",
        "",
        "[[4,4],4,4]",
        "[[4,4],4,4,4]",
        "",
        "[7,7,7,7]",
        "[7,7,7]",
        "",
        "[]",
        "[3]",
        "",
        "[[[]]]",
        "[[]]",
        "",
        "[1,[2,[3,[4,[5,6,7]]]],8,9]",
        "[1,[2,[3,[4,[5,6,0]]]],8,9]",
        ""
    ], 140),
]

class TestSolution(unittest.TestCase):
    def test_day_13_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_compareLR(self):
        for testCase in tests_compareLR:
            self.assertEqual(compareLR(testCase[0][0],testCase[0][1]), testCase[1], f"error comparing ({testCase[0][0]}) to ({testCase[0][1]})")

    def test_day_13_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()