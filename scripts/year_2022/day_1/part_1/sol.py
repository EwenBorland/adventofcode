def solution(input):
    return max(get_elf_list(input))

def get_elf_list(input):
    elves = []
    elf = 0
    for line in input:
        
        if line in ["","\n","\r","\r\n","\n\r"]:
            elves.append(elf)
            elf=0
        else:
            elf += int(line)
    return elves
