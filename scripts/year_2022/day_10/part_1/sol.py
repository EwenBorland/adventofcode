def doCycle(X, action, value):
    match action:
        case "noop":
            return X
        case "addX":
            return X+value

def parseInput(input):
    actions=[]
    for line in input:    
        length = len(line)
        actions.append(("noop", 0)) # noop, or cycle 1 of addx
        if length != 4:
            actions.append(("addX", int(line[5:length]))) # cycle 2 of addx
    return actions

def solution(input):
    X=1
    sumOfStrengths=0
    for cycle, action in enumerate(parseInput(input),1):
        if cycle % 20 == 0:
            print(f'start of cycle: {cycle}, X: {X}')
            if cycle in [20,60,100,140,180,220]:
                sumOfStrengths += cycle*X 
        X = doCycle(X, action[0], action[1])

    return sumOfStrengths