shape_scores = {
    "A": 1,
    "B": 2,
    "C": 3
}

outcome_scores = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

hand_mapping = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

outcome_mapping = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

def get_total_score(shape, outcome):
    return shape_scores[shape] + outcome_scores[outcome]

'''
ABC
XYZ

Z(C) beats B
Y(B) beats A
X(A) beats C

'''

def get_outcome(you_hand, opponent_hand):
    if you_hand == opponent_hand:
        return "draw"
    match opponent_hand:
        case "A":
            return "win" if you_hand == "B" else "lose"
        case "B":
            return "win" if you_hand == "C" else "lose"
        case "C":
            return "win" if you_hand == "A" else "lose"

def parse_line(line):
    l = line.strip("\n").split(" ")
    return l[0], l[1]

def solution(input):
    your_score = 0
    for line in input:
        opponents_hand, your_hand = parse_line(line) 
        your_hand = hand_mapping[your_hand]
        outcome = get_outcome(your_hand, opponents_hand)
        your_score += get_total_score(your_hand, outcome)
    return your_score
