from ..part_1.sol import get_outcome, parse_line, get_total_score, outcome_mapping

def pick_outcome(opponents_hand, ideal_outcome):
    if ideal_outcome == "draw":
        return opponents_hand
    
    match opponents_hand:
        case "A":
            return "B" if ideal_outcome == "win" else "C"
        case "B":
            return "C" if ideal_outcome == "win" else "A"
        case "C":
            return "A" if ideal_outcome == "win" else "B"

def solution(input):
    your_score = 0
    for line in input:
        opponents_hand, ideal_outcome = parse_line(line) 
        your_hand = pick_outcome(opponents_hand, outcome_mapping[ideal_outcome])
        outcome = get_outcome(your_hand, opponents_hand)
        your_score += get_total_score(your_hand, outcome)
    return your_score
