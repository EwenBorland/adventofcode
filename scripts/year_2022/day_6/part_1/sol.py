def solution(input):
    stream = input[0]
    for i in range(3,len(stream),1):
        # chars = stream[i-4:i]
        # s = set(chars)
        # ls = len(s)

        # print(f'chars: {chars}, set: {s}, lenset: {ls}')
        if len(set(stream[i-4:i])) == 4:
            return i
    return 0
