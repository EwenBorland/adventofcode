from ..part_1.sol import solution as p1sol

def solution(input):
    input_in_threes = []
    n_entries = len(input)
    for i in range(n_entries - 2):
        input_in_threes.append(int(input[i]) + int(input[i+1]) + int(input[i+2]))
    increases = p1sol(input_in_threes)
    return increases
