class Stack:
    def __init__(self, input):
        self.stack = input
    
    def add(self, box):
        self.stack.insert(0,box) 

    def remove(self):
        if len(self.stack) == 0:
            return ""
        box = self.stack.pop(0)
        return box
    
    def move(self, amount, toStack):
        for _ in range(amount):
            box = self.remove()
            if box == "":
                continue
            toStack.add(box)

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
        stacks[int(f)].move(int(m), stacks[int(t)])

    print("END")
    tops = ""
    for key, stack in stacks.items():
        print(f'key: {key}, stack: {stack.stack}')
        tops += stack.stack[0]

    print(f'tops:{tops}')
    return stacks
