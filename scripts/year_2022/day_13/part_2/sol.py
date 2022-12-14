from ..part_1.sol import parseAsTuples, compareLR
from functools import cmp_to_key

def parseAsList(input):
    packets = []
    for i in range(0,len(input),3):
        packets.append(eval(input[i]))
        packets.append(eval(input[i+1]))
    
    packets.append([[2]])
    packets.append([[6]])

    return packets

def compareLRTwo(l,r):
    leftFirst, _ = compareLR(l,r)

    if leftFirst:
        return -1
    return 1

def solution(input):
    packets = parseAsList(input)
    packetsSorted = sorted(packets, key=cmp_to_key(compareLRTwo))

    for i, packet in enumerate(packetsSorted,1):
        if packet == [[2]]:
            divPacketOne = i
        if packet == [[6]]:
            divPacketTwo = i

    return divPacketOne * divPacketTwo