class Tree:
    def __init__(self, h):
        self.height=h
        self.seen= True 

def solution(input):
    forest = []
    for line in input:
        row = [Tree(int(tree_height)) for tree_height in line]
        forest.append(row)

    rows = len(forest)
    columns = len(forest[0])
    print(f"total trees: {rows*columns}")

    for r in range(rows):
        for c in range(columns):
            tree = forest[r][c]
            treesLeft = forest[r][0:c]
            treesRight = forest[r][c+1:columns]
            treesUp = [forest[i][c] for i in range(0,r)]
            treesDown = [forest[i][c] for i in range(r+1,rows)]
            
            seenLeft, seenRight, seenUp, seenDown = True, True, True, True

            for t in treesLeft:
                if len(treesLeft) == 0:
                    break
                if tree.height <= t.height:
                    seenLeft = False
            for t in treesRight:
                if len(treesRight) == 0:
                    break
                if tree.height <= t.height:
                    seenRight = False
            for t in treesUp:
                if len(treesUp) == 0:
                    break
                if tree.height <= t.height:
                    seenUp = False
            for t in treesDown:
                if len(treesDown) == 0:
                    break
                if tree.height <= t.height:
                    seenDown = False
            
            if not (seenLeft or seenRight or seenUp or seenDown):
                tree.seen = False
    
    # for r in forest:
    #     print("\n")
    #     print(f'{[c.seen for c in r]}')
            
    treesSeen = 0
    treesHidden = 0
    for r in forest:
        for t in r:
            if t.seen:
                treesSeen += 1
            else:
                treesHidden += 1
    return treesSeen
