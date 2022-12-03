from ..part_1.sol import get_duplicate_items, sum_priorities

def solution(input):
    badges = []
    for group in (input[i:i+3] for i in range(0, len(input), 3)):
        dup_a = get_duplicate_items(group[0], group[1])
        dup_b = get_duplicate_items(group[0], group[2])
        badge = get_duplicate_items(dup_a, dup_b)
        badges.append(badge[0])

    print(badges)
    return sum_priorities(badges) 
