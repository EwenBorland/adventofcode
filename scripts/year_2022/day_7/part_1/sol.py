def getLineType(line):
    match line[0]:
        case"$":
            return "command"
        case "d":
            return "dir"
        case _:
            return "file"

def dir_path(cursorPosition):
    name = ""
    for p in cursorPosition:
        name += p
    return name

def solution(input):
    cursorPosition = []
    directories = {}

    for line in input:
        t = getLineType(line)
        l = line.split(" ")
        if t == "command":
            # command(line, cursorPosition) # cd .., cd dirname, ls
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
    
    
    for key, value in directories.items():
        print(f'key: {key}, value: {value}')
    
    maxSize = 100000

    totalSize = 0
    for dirSize in directories.values():
        if dirSize <= maxSize:
            totalSize += dirSize
    
    return totalSize
    