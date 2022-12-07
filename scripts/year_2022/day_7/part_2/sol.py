from ..part_1.sol import getLineType, dir_path

def solution(input):
    cursorPosition = []
    directories = {}

    for line in input:
        t = getLineType(line)
        l = line.split(" ")
        if t == "command":
            if l[1] == "cd":
                if l[2] == "..":
                    cursorPosition.pop(0)
                else:
                    cursorPosition.insert(0, l[2])
            if not dir_path(cursorPosition) in directories:
                directories[dir_path(cursorPosition)] = 0
        elif t == "file":
            fileSize = int(l[0])
            for i in range(len(cursorPosition)):
                directories[dir_path(cursorPosition[-i:])] += fileSize
    
    maxSize = 100000
    totalSpace = 70000000
    requiredSpace = 30000000
    freeSpace = totalSpace - directories["/"]

    minRequiredDeletion = requiredSpace - freeSpace
    bestOption = 100000000000
    for dirSize in directories.values():
        if dirSize - minRequiredDeletion > 0 and dirSize < bestOption and dirSize >= minRequiredDeletion:
                bestOption =dirSize
    return bestOption