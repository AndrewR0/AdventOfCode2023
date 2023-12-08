
def pairings(hand, individual_cards, line):
    if len(individual_cards) == 1:
        return "6" + line
    elif len(individual_cards) == 2:
        for _ in hand:
            if hand.count(_) == 4:
                return "5" + line
        else:
            return "4" + line
    elif len(individual_cards) == 3:
        for _ in hand:
            if hand.count(_) == 3:
                return "3" + line
        return "2" + line
    elif len(individual_cards) == 4:
        return "1" + line
    else:
        return "0" + line

hands = []
with open("Day7/input.txt", "r") as file:
    while line := file.readline():
        
        line = line.strip().split(" ")[0].translate(str.maketrans('AKQJT98765432', 'MLKJIHGFEDCBA')) + " " + line.strip().split(" ")[1]
        hand = line.split(" ")[0]
        hand_set = set(hand)

        hands.append(pairings(hand, hand_set, line))

hands.sort()
total = 0
for index, hand in enumerate(hands):
    total += int(hand.split(" ")[1]) * (index+1)

print(total)