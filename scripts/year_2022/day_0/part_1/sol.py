def solution(input):
    increases = 0
    elses = 0
    depth = int(input[0])
    for line in input[1:]:
        if int(line) > depth:
            increases += 1
        else:
            elses += 1    
        depth = int(line)
    print(f'increases: {increases}, elses: {elses}, sum: {increases+elses}')
    return increases
