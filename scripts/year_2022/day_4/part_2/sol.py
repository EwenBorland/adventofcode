from ..part_1.sol import solution as sol1

def compare_pair_outside(s,a=False):
    pair = s.split(",")
    range_1, range_2 = [int(i) for i in pair[0].split("-")], [int(i) for i in pair[1].split("-")]

    if range_1[0] > range_2[1] :
        return False

    if range_1[1] < range_2[0]:
         return False
    
    return True

def solution(input):
    part_containment = 0
    for line in input:
        if compare_pair_outside(line):
            # print(f'pair: {line}')
            part_containment += 1
    return part_containment
