def parseAsTuples(input):
    pairs = []
    for i in range(0,len(input),3):
        pairs.append((eval(input[i]),eval(input[i+1])))

    return pairs

def compareIntInt(l,r):
    if l == r:
        # print(f'II: Compare {l} vs {r}, F F')
        return False, False
    # print(f'II: Compare {l} vs {r}, ? T')
    return r > l, True

def compareListList(l,r):
    lenl, lenr = len(l), len(r)
    # print(f'LL: Compare {l} vs {r}')
    for pair in zip(l,r):
        a, b = checkInts(pair[0],pair[1])
        if a and b:
            correct, br = compareIntInt(pair[0],pair[1])
        else:
            correct, br = compareLR(pair[0],pair[1])
        if br:
            return correct, br
    
    # no conclusion, or ran out
    if lenl == lenr:
        return False, False
    
    return lenr > lenl, True

def compareIntList(l,r):
    return compareListList([l],r)

def compareListInt(l,r):
    return compareListList(l,[r])

def compareLR(l,r):
    lInt, rInt = checkInts(l,r)
    if lInt:
        if rInt:
            return compareIntInt(l,r)
        else:
            return compareIntList(l,r)
    
    if rInt:
        return compareListInt(l,r)
    
    return compareListList(l,r)

def checkInts(l,r,):
    return type(l) == int, type(r) == int

def solution(input):
    sumOfCorrectIndices = 0
    pairs = parseAsTuples(input)
    for count, pair in enumerate(pairs,1):
        correct, _ = compareLR(pair[0],pair[1])
        # print(f"count: {count}, correct: {correct}")
        if correct:
            sumOfCorrectIndices += count

    return sumOfCorrectIndices