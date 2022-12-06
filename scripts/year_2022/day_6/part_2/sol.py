def solution(input):
    stream = input[0]
    for i in range(13,len(stream),1):
        # chars = stream[i-14:i]
        # s = set(chars)
        # ls = len(s)

        # print(f'chars: {chars}, set: {s}, lenset: {ls}')
        if len(set(stream[i-14:i])) == 14:
            return i
    return 0