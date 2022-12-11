import math

class Monkey:
    def __init__(self, items, operation, decision):
        self.items = items
        self.operation = operation
        self.decision = decision
        self.inspections = 0
    
    def inspect(self, i):
        self.items[i] = self.operation(self.items[i])
        self.inspections += 1
    
    def throw(self, i):
        reciever = self.decision(self.items[i])
        return reciever

    def startTurn(self):
        for i in range(len(self.items)):
            self.inspect(i)
    
    def endTurn(self):
        self.items = []

def getMonkeys():
    m = []
    m.append(Monkey([75, 75, 98, 97, 79, 97, 64], lambda old: math.floor((old * 13)/3), lambda new: 2 if new % 19 == 0 else 7))
    m.append(Monkey([50, 99, 80, 84, 65, 95], lambda old: math.floor((old + 2)/3), lambda new: 4 if new % 3 == 0 else 5))
    m.append(Monkey([96, 74, 68, 96, 56, 71, 75, 53], lambda old: math.floor((old + 1)/3), lambda new: 7 if new % 11 == 0 else 3))
    m.append(Monkey([83, 96, 86, 58, 92], lambda old: math.floor((old + 8)/3), lambda new: 6 if new % 17 == 0 else 1))
    m.append(Monkey([99], lambda old: math.floor((old * old)/3), lambda new: 0 if new % 5 == 0 else 5))
    m.append(Monkey([60, 54, 83], lambda old: math.floor((old + 4)/3), lambda new: 2 if new % 2 == 0 else 0))
    m.append(Monkey([77, 67], lambda old: math.floor((old * 17)/3), lambda new: 4 if new % 13 == 0 else 1))
    m.append(Monkey([95, 65, 58, 76], lambda old: math.floor((old + 5)/3), lambda new: 3 if new % 7 == 0 else 6))
    return m
    

def solution(input):
    # input is hardcoded instead
    monkeys = getMonkeys()

    for _ in range(20):
        for monkey in monkeys:
            monkey.startTurn()
            for i in range(len(monkey.items)):
                receiver = monkey.throw(i)
                monkeys[receiver].items.append(monkey.items[i])
            monkey.endTurn()
    
    print("completed 20 rounds")
    for m in range(len(monkeys)):
        print(f'Monkey {m} inspected items {monkeys[m].inspections} times.')
    
    inspections = [m.inspections for m in monkeys]
    inspections.sort(reverse=True)

    print(f"inspections: {inspections}")

    return inspections[0]*inspections[1]