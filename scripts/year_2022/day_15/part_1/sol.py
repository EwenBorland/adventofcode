# for each sensor, calulate the coordinates that cannot be beacons
# store these coordinates in a map[row][list of notBeacon cols]

def addToMap(map, row, col):
    # print(f'row:{row}')
    map.setdefault(row,list()).append(col)

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

def solution(input, concernedY=2000000):
    caveMap = {}
    sensors = {}
    beacons = {}

    for line in input:
        sensorX, sensorY, beaconX, beaconY = parseLine(line) 
        print(f'starting line : {line}')
        addToMap(sensors, sensorY, sensorX)
        addToMap(beacons, beaconY, beaconX)
        beaconDistance = taxiDistance(sensorX, sensorY, beaconX, beaconY)

        for y in range(-beaconDistance, beaconDistance, 1):
            if sensorY+y != concernedY:
                continue
            xVariance = beaconDistance - abs(y)
            for x in range(-xVariance, xVariance, 1):
                addToMap(caveMap, sensorY+y, sensorX+x)

    return len(set(caveMap[concernedY]))