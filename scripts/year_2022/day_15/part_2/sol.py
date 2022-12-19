def removeFromMap(map, row, col):
    # print(f'row:{row}')
    if col in map[row]: map[row].remove(col)

def parseLine(line):
    # Sensor at x=2662540, y=1992627: closest beacon is at x=1562171, y=2000000
    xS = line.split("x=")
    sensorX = int(xS[1].split(",")[0])
    beaconX = int(xS[2].split(",")[0])

    yS = line.split("y=")
    sensorY = int(yS[1].split(":")[0])
    beaconY = int(yS[2].split(",")[0])

    return sensorX, sensorY, beaconX, beaconY

def taxiDistance(point1X, point1Y, point2X, point2Y):
    xDistance = abs(point1X-point2X)
    yDistance = abs(point1Y-point2Y)

    return xDistance+yDistance

def solution(input, limit=4000000):
    caveMap = [[i for i in range(limit)] for _ in range(limit)]

    for line in input:
        sensorX, sensorY, beaconX, beaconY = parseLine(line) 
        print(f'starting line : {line}')
        beaconDistance = taxiDistance(sensorX, sensorY, beaconX, beaconY)

        for y in range(-beaconDistance, beaconDistance, 1):
            if sensorY+y >= limit:
                continue
            xVariance = beaconDistance - abs(y)
            for x in range(-xVariance, xVariance, 1):
                if sensorX+x >= limit:
                    continue
                removeFromMap(caveMap, sensorY+y, sensorX+x)
    
    for c, r in enumerate(caveMap):
        beaconX, beaconY
        if len(r) != 0:
            beaconY = c+1
            beaconX = r[0]
            print(f'found beacon at [{beaconX}, {beaconY}]')
            break

    return (beaconX*4000000) + beaconY