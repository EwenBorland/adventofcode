#Boundaries: [493,15],[567,172]

def findBoundaries(input):
    maxX, minX, maxY, minY = 0,1000,0,1000
    for line in input:
        coordinates = line.split("->")
        for coord in coordinates:
            splitCoords = [int(x) for x in coord.split(",")]
            maxX = max(maxX, splitCoords[0])
            minX = min(minX, splitCoords[0])
            maxY = max(maxY, splitCoords[1])
            minY = min(minY, splitCoords[1])
    print(f'Min X: {minX}\nMax X: {maxX}\nMin Y: {minY}\nMax Y: {maxY}')
    return minX, maxX, minY, maxY

def calculateLine(startCoord, endCoord):
    '''
    returns a list of coordinates in a line between startCoord and endCoord
    '''
    if startCoord[0] == endCoord[0]:
        # horizontal line
        return [[endCoord[0],y] for y in range(min(startCoord[1],endCoord[1]),max(startCoord[1],endCoord[1])+1,1)]
    # vertical line
    return [[x,endCoord[1]] for x in range(min(startCoord[0],endCoord[0]),max(startCoord[0],endCoord[0])+1,1)]

def drawLines(coordinates, cave):
    for i in range(len(coordinates)-1):
        rocks = calculateLine(coordinates[i],coordinates[i+1])
        # print(rocks)
        for rock in rocks:
            # print(f'rock{rock}')
            cave[rock[1]][rock[0]] = "#"
    return cave

def renderCave(cave,minY, maxY, minX, maxX):
    for row in cave[0:maxY+2]:
        line = ""
        for c in row[minX-3:maxX+3]: line += c
        print(line)

def BRINGONTHESAND(cave):
    iterations = 0
    while iterations < 10000:
        sandAtRest = simulateSand(cave)
        # print("yabadabadoo")
        if not sandAtRest:
            break
        iterations += 1
    return iterations

def simulateSand(cave):
    sandCoord = [500,0]
    for _ in range(10000):
        nextCoord = [sandCoord[0], sandCoord[1]+1]
        try:
            nextSymbol = cave[nextCoord[1]][nextCoord[0]]
            # print(f"Next: {nextCoord}, nextSymbol: {nextSymbol}")
        except IndexError:
            print(f"Next: {nextCoord}")
            raise(IndexError)
        match nextSymbol:
            case "e":
                return False
            case ".":
                sandCoord = nextCoord
            case "#" | "o":
                if cave[nextCoord[1]][nextCoord[0]-1] not in ["#","o"]:
                    sandCoord = [nextCoord[0]-1, nextCoord[1]]
                    continue
                elif cave[nextCoord[1]][nextCoord[0]+1] not in ["#","o"]:
                    sandCoord = [nextCoord[0]+1, nextCoord[1]]
                    continue
                else:
                    cave[sandCoord[1]][sandCoord[0]] = "o"
                    return True
            case _:
                print(f"Unknown Symbol: {nextSymbol}")

    return False
def solution(input):
    minX, maxX, minY, maxY = findBoundaries(input)
    cave = [["." for _ in range(maxX+600)] for _ in range(maxY+4)] # create cave of air
    for line in input:
        coordinates = line.split("->")
        coordinates= [[int(x) for x in coord.split(",")] for coord in coordinates]
        cave = drawLines(coordinates,cave)
    # cave[minY-1][500] = "S"
    cave[maxY+2] = ["e" for _ in range(maxX+600)]
    renderCave(cave, minY, len(cave), minX, maxX)
    sands = BRINGONTHESAND(cave)
    
    return sands