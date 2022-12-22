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

def gapInRanges(ranges,limit):
    currentIndex = 0
    found = False
    while currentIndex < limit:
        for c, r in enumerate(ranges):
            found = True
            r0, r1 = min(r), max(r)
            if r0 <= currentIndex and r1 >= currentIndex:
                currentIndex = r1 + 1
                ranges.pop(c)
                found = False
                break
        if found:
            return True, currentIndex
    return False, 0


def solution(input, limit=4000000):
    caveMap = [[] for _ in range(limit)]

    for line in input:
        sensorX, sensorY, beaconX, beaconY = parseLine(line) 
        print(f'starting line : {line}')
        beaconDistance = taxiDistance(sensorX, sensorY, beaconX, beaconY)
    
        for by in range(-beaconDistance, beaconDistance, 1):
            y = sensorY + by
            if y < 0 or y >= limit:
                continue
            xVariance = beaconDistance - abs(by)

            caveMap[y].append([sensorX-xVariance, sensorX+xVariance])

    
    for c, r in enumerate(caveMap):
        found, index = gapInRanges(r, limit)
        if found:
            print(f'found not beacon at [{index}, {c}]')
            return (index*4000000) + c

    return 0