SIZECALLS = 0
class File:
    def __init__(self,name, size):
        self.name = name
        self.size = size

class Dir:
    def __init__(self, files, name):
        self.dirs = []
        self.size = 0
        self.filesSize = 0
        self.name = name
        for f in files:
            self.addFile(f)
        self.final = False
        # self.getSize()
        
    
    def getSize(self, parents, dirs=None,final=False):
        # global SIZECALLS
        # SIZECALLS += 1
        # print(f'getSize called {SIZECALLS} times, currently in {self.name}')
        print(f'paretasdsad : [ {parents} ]')

        if self.name in parents:
            return 0

        if self.final:
            return self.size
        self.size = self.filesSize
        


        for dName in self.dirs:
            if not dName in dirs:
                continue
            if dirs[dName].final:
                child_size = dirs[dName].size
            else:
                parents = parents.append(self.name)
                child_size = dirs[dName].getSize(parents,dirs=dirs,final=final)
            # print(f'child: {dName}, size: {child_size}')
            self.size += child_size
        
        # print(f'size: {self.size}')
        self.final = final
        return self.size
    
    def addFile(self, f):
        self.filesSize += f.size
        # self.getSize(dirs)

    def addDir(self, d):
        if d not in self.dirs and d != self.name:
            self.dirs.append(d)
        # self.getSize(dirs)
        
class Cursor:
    def __init__(self, pos):
        self.pos = pos
        self.tree = [pos]

    def moveIn(self, dirName):
        self.tree.insert(0,dirName)
        self.pos = dirName
    
    def moveOut(self):
        self.tree.pop(0)
        self.pos = self.tree[0]
    
    def reset(self, dirName):
        self.__init__(dirName)

    def move(self, dirName):
        # print(f'Moving cursor from: {self.pos}, to: {dirName}')
        match dirName:
            case "/":
                self.reset(dirName)
            case "..":
                self.moveOut()
            case _:
                self.moveIn(dirName)


def getLineType(line):
    match line[0]:
        case"$":
            return "command"
        case "d":
            return "dir"
        case _:
            return "file"
        
def command(line, cursor, dirs):
    l = line.split(" ")
    if l[1] == "cd":
        cursor.move(l[2])
    if l[1] == "ls":
        if not cursor.pos in dirs:
            dirs[cursor.pos] = Dir([], cursor.pos)



def file(line, cursor, dirs):
    l = line.split(" ")
    fileSize = int(l[0])
    fileName = l[1]

    f = File(fileName, fileSize)

    dirs[cursor.pos].addFile(f)

def dir(line, cursor, dirs):
    dirs[cursor.pos].addDir(line.split(" ")[1])

def solution(input):
    cursor = Cursor("/")
    dirs = {}

    for line in input:
        t = getLineType(line)
        if t == "command":
            command(line, cursor,dirs)
        elif t == "dir":
            dir(line, cursor, dirs)
        elif t == "file":
            file(line, cursor, dirs)
        else:
            print(f'UNEXPECTED COMMAND {line}')
    
    totalSize = 0
    print(len(dirs.values()))
    for key, value in dirs.items():
        if key == "/":
            continue
        if value.final:
            dSize = value.size
        else:
            dSize = value.getSize(["",""],dirs=dirs, final=True)

        if dSize <= 100000:
            totalSize += dSize
    

    if dirs["/"].final:
        dSize = value.size
    else:
        dSize = dirs["/"].getSize(["",""], dirs=dirs, final=True)

    if dSize <= 100000:
        totalSize += dSize
            
    return totalSize
