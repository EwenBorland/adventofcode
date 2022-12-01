from ..part_1.sol import get_elf_list

def solution(input):
    elves = get_elf_list(input)
    elves.sort()
    maxThree = elves[-3:]
    print(f'The top elves have {maxThree} calories')
    return sum(maxThree)
