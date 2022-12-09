class Tree:
    def __init__(self, h):
        self.height=h
        self.seen=True 
        self.score=0

def solution(input):
    forest = []
    for line in input:
        row = [Tree(int(tree_height)) for tree_height in line]
        forest.append(row)

    rows = len(forest)
    columns = len(forest[0])
    print(f"total trees: {rows*columns}")

    bestScore = 0
    for r in range(rows):
        for c in range(columns):
            if r == 0 or r == rows or c == 0 or c == columns:
                continue # trees on edge have 0 score

            tree = forest[r][c]
            treesLeft = forest[r][0:c]
            treesRight = forest[r][c+1:columns]
            treesUp = [forest[i][c] for i in range(0,r)]
            treesDown = [forest[i][c] for i in range(r+1,rows)]
            treesVisible = [0,0,0,0]

            for t in treesLeft[::-1]:
                treesVisible[0] += 1
                if t.height >= tree.height:
                    break
            
            for t in treesRight:
                treesVisible[1] += 1
                if t.height >= tree.height:
                    break
            
            for t in treesUp[::-1]:
                treesVisible[2] += 1
                if t.height >= tree.height:
                    break
            
            for t in treesDown:
                treesVisible[3] += 1
                if t.height >= tree.height:
                    break
            
            score = treesVisible[0] * treesVisible[1] * treesVisible[2] * treesVisible[3]
            bestScore = max(bestScore,score)
    return bestScore
