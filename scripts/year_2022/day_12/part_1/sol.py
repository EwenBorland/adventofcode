class node:
    def __init__(self,height):
        self.height = height
        self.been = False
        self.score = 0

def parseInput(input):
    heightMap = []
    startCoords, endCoords = (0,0), (0,0)
    for i, line in enumerate(input):
        l = [node(ord(x)-96) for x in line]
        for j, num in enumerate(l):
            if num.height == -13:
                startCoords = (i,j)
                l[j].height = 1
            if num.height == -27:
                endCoords = (i,j)
                l[j].height = 26
        heightMap.append(l)
    return heightMap, startCoords, endCoords

def getAdjacent(listOfCoords,heightMap,maxI,maxJ):

    adjacentCoords = []
    for l in listOfCoords:
        up, down, left, right = l[0]-1, l[0]+1, l[1]-1, l[1]+1

        if up >=0 and isViable(heightMap[l[0]][l[1]],heightMap[up][l[1]]):
            adjacentCoords.append((up,l[1]))
        if down <maxI and isViable(heightMap[l[0]][l[1]],heightMap[down][l[1]]):
            adjacentCoords.append((down,l[1])) 
        if left >=0 and isViable(heightMap[l[0]][l[1]],heightMap[l[0]][left]):
            adjacentCoords.append((l[0],left)) 
        if right < maxJ and isViable(heightMap[l[0]][l[1]],heightMap[l[0]][right]):
            adjacentCoords.append((l[0],right))

    return adjacentCoords

def isViable(position, adjacent):
    if adjacent.been:
        return False
    
    if (position.height - adjacent.height) > 1:
        return False
    
    return True

def solution(input):
    heightMap, start, end = parseInput(input)
    maxI, maxJ = len(heightMap), len(heightMap[0])
    print(f'starting at: {start}, ending at: {end}')
    
    # starting at end
    pathCoords = [end]
    steps = 1
    while True:

        newCoords = getAdjacent(pathCoords, heightMap, maxI, maxJ)
        
        if start in newCoords:
            break
        
        steps += 1
        pathCoords = list(set(newCoords))

    return steps