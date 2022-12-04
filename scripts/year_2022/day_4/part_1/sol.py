import string

def compare_pair(s,a=False):
    pair = s.split(",")
    range_1, range_2 = [int(i) for i in pair[0].split("-")], [int(i) for i in pair[1].split("-")]

    if range_1[0] > range_2[0] :#first_is_bigger
        if range_1[1] > range_2[1]:
            return False

    if range_1[0] < range_2[0]:
        if range_1[1] < range_2[1]:
            return False
    
    return True

def solution(input):
    full_containment = 0
    for line in input:
        if compare_pair(line):
            # print(f'pair: {line}')
            full_containment += 1
    return full_containment
