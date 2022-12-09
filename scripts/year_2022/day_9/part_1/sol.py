def initMap(size):
    return [[False for _ in range(size)] for _ in range(size)]

def distance(a,b):
    if a[0]-b[0] >= 2:
        return True
    if a[0]-b[0] <= -2:
        return True
    if a[1]-b[1] >= 2:
        return True
    if a[1]-b[1] <= -2:
        return True
    return False

def solution(input):
    offset = 1000
    positionMap = initMap(offset*2)
    positionMap[offset][offset] = True # starting position
    headPosition = [offset,offset]
    tailPosition = [offset,offset]
    for line in input:
        direction = line[0]
        for _ in range(int(line[2:])):
            match direction:
                case "U":
                    newHeadPosition = [headPosition[0],headPosition[1]+1]
                case "D":
                    newHeadPosition = [headPosition[0],headPosition[1]-1]
                case "R":
                    newHeadPosition = [headPosition[0]+1,headPosition[1]]
                case "L":
                    newHeadPosition = [headPosition[0]-1,headPosition[1]]
                case _:
                    print(f"invalid move: {direction}")

            if distance(tailPosition, newHeadPosition):
                tailPosition = headPosition

            headPosition = newHeadPosition
            # print(f'tail: {tailPosition}, head: {headPosition}, map : {positionMap}')
            positionMap[tailPosition[0]][tailPosition[1]]= True

    positions = 0
    for x in positionMap:
        for y in x:
            if y:
                positions += 1
    
    return positions
