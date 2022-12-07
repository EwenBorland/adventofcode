import unittest
from scripts.year_2022.day_7.part_1.sol import solution as sol1
from scripts.year_2022.day_7.part_2.sol import solution as sol2

tests_1 = [
    (["$ cd /", "$ ls","dir a","14848514 b.txt","8504156 c.dat","dir d","$ cd a","$ ls","dir e","29116 f","2557 g","62596 h.lst","$ cd e","$ ls","584 i","$ cd ..","$ cd ..","$ cd d","$ ls","4060174 j","8033020 d.log","5626152 d.ext","7214296 k"], 95437),
    (["$ cd /", "$ ls","dir a","100 b.txt","$ cd a","$ ls","25 f","65 g"], 280),
    (["$ cd /", "$ ls","dir a","100 b.txt","dir aa","$ cd a","$ ls","25 f","65 g", "$ cd ..", "$ cd aa", "$ ls", "33 oogieboogie.groove"], 346)
]


tests_2 = [
    (["mjqjpqmgbljsphdztnvjfqwrcgsmlb"], 19),
    (["bvwbjplbgvbhsrlpgdmjqwftvncz"], 23),
    (["nppdvjthqldpwncqszvftbrmjlhg"], 23),
    (["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"], 29),
    (["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"], 26)
]

class TestSolution(unittest.TestCase):
    def test_day_7_1(self): 
        for testCase in tests_1:
            self.assertEqual(sol1(testCase[0]), testCase[1])
    
    def test_day_7_2(self): 
        for testCase in tests_2:
            self.assertEqual(sol2(testCase[0]), testCase[1])
        
if __name__ == "__main__":
    unittest.main()