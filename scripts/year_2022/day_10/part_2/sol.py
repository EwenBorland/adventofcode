from ..part_1.sol import parseInput, doCycle

def printCrt(crt):
    print("|========================================|")
    for i in range(0, len(crt), 40):
        print(f'|{crt[i:i+40]}|') 
    print("|========================================|")

def solution(input):
    position=2
    crtX = 0
    crt = ""
    for cycle, action in enumerate(parseInput(input),1):
        crtX+=1
        if crtX == 41:
            crtX = 1
        if crtX in [position, position-1, position+1]:
            crt += "#"
        else:
            crt += "."  

        position = doCycle(position, action[0], action[1])

    printCrt(crt)
    return crt