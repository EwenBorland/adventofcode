class Stack:
    def __init__(self, input):
        self.stack = input
    
    def add(self, box):
        # print(f'adding boxes:{box} to stack:{self.stack}')
        self.stack = box + self.stack 
        # print(f'result stack:{self.stack}')

    def remove(self, amount):
        boxes = []
        for _ in range(amount):
            if len(self.stack) == 0:
                continue
            boxes.append(self.stack.pop(0))
        return boxes
    
    def move(self, amount, toStack):
        # print(f'moving {amount} boxes')
        boxes = self.remove(amount)
        if len(boxes) == 0:
            return
        toStack.add(boxes)

def parse_input(input):
    header = input.pop(0)
    stacks = {}
    instructions = []
    for c in header:
        if c != " ":
            stacks[int(c)] = []
    
    blank = True
    for line in input:
        if blank:
            blank = False
            for i in range(0, len(line), 4):
                if line[i] == "[":
                    stacks[int(i/4)+1].append(line[i+1])
                    blank = True 
        else:
            # line.replace("move ", "").replace("from ", "").replace("to ", "")
            instructions.append(line.split(" "))

    return stacks, instructions

def solution(input):
    stacks = {}

    stacksList, instructions = parse_input(input)

    for c, s in enumerate(stacksList.values()):
        stacks[c+1] = Stack(s)

    print("START")
    for key, stack in stacks.items():
        print(f'key: {key}, stack: {stack.stack}')
    
    for l in instructions:
        m, f, t = l[1], l[3], l[5]
        # print(f'instructions: {l}, parsed: m:{m} f:{f} t:{t}')
        stacks[int(f)].move(int(m), stacks[int(t)])

    print("END")
    tops = ""
    for key, stack in stacks.items():
        print(f'key: {key}, stack: {stack.stack}')
        tops += stack.stack[0]

    print(f'tops:{tops}')
    return stacks