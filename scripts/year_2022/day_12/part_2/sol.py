from ..part_1.sol import parseInput, getAdjacent

def solution(input):
    heightMap, start, end = parseInput(input)
    maxI, maxJ = len(heightMap), len(heightMap[0])
    print(f'starting at: {start}, ending at: {end}')
    
    # starting at end
    pathCoords = [end]
    steps = 0
    home = False
    while not home:

        newCoords = getAdjacent(pathCoords, heightMap, maxI, maxJ)
        
        for coord in newCoords:
            if heightMap[coord[0]][coord[1]].height == 1:
                home = True
                break
        
        steps += 1
        pathCoords = list(set(newCoords))

    return steps