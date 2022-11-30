from scripts import helpers
import importlib

class Puzzle:
    def __init__(self):
        self.year, self.day, self.part = helpers.parse_args()
        self.input = helpers.loadInput(self.year, self.day, self.part)
    
    def validate(self):
        if self.year == 0:
            return False
        if len(self.input) == 0:
            return False
        return True

    def run(self):
        sol = importlib.import_module(f'scripts.year_{self.year}.day_{self.day}.part_{self.part}.sol')
        return sol.solution(self.input)
