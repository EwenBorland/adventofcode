from ..part_1.sol import findBoundaries, drawLines, renderCave

def BRINGONTHESAND(cave):
    iterations = 0
    while iterations < 100000:
        sandAtRest = simulateSand(cave)
        # print("yabadabadoo")
        if not sandAtRest:
            break
        iterations += 1
    return iterations

def simulateSand(cave):
    sandCoord = [500,0]
    if cave[0][500] == "o":
        return False
    for _ in range(100000):
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
    cave[maxY+2] = ["#" for _ in range(maxX+600)]
    renderCave(cave, minY, len(cave), minX, maxX)
    sands = BRINGONTHESAND(cave)
    
    return sands