from collections import namedtuple
Hand = namedtuple("Hand", ["rank", "bid", "cards"])

def main():
    file = open("input.txt", "r")
    lines = file.readlines()

    # LOGIC 1
    hands1 = []
    for line in lines:
        hand = line[:5]
        bid = int(line[6:])
        hands1.append(identify_hand(hand, bid))

    order_hands(hands1)
    total1 = 0
    for i, hand in enumerate(hands1):
        total1 += hand.bid * (len(hands1) - i)

    print(f"First answer: {total1}")

    # LOGIC 2
    hands2 = []
    for line in lines:
        hand = line[:5]
        bid = int(line[6:])
        hands2.append(identify_hand2(hand, bid))

    order_hands(hands2)
    total2 = 0
    for i, hand in enumerate(hands2):
        total2 += hand.bid * (len(hands2) - i)

    print(f"Second answer: {total2}")

def identify_hand(hand, bid, card_numbers = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]):
    temp = 0
    for c in card_numbers:
        count = hand.count(c)
        if count == 5:
            return Hand(0, bid, [card_numbers.index(card) for card in [char for char in hand]])
        elif count == 4:
            return Hand(1, bid, [card_numbers.index(card) for card in [char for char in hand]])
        elif count == 3:
            if temp == 2:
                return Hand(2, bid, [card_numbers.index(card) for card in [char for char in hand]])
            else:
                temp = 3
        elif count == 2:
            if temp == 3:
                return Hand(2, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif temp == 2:
                return Hand(4, bid, [card_numbers.index(card) for card in [char for char in hand]])
            else:
                temp = 2
    if temp == 3:
        return Hand(3, bid, [card_numbers.index(card) for card in [char for char in hand]])
    elif temp == 2:
        return Hand(5, bid, [card_numbers.index(card) for card in [char for char in hand]])
    return Hand(6, bid, [card_numbers.index(card) for card in [char for char in hand]])

def identify_hand2(hand, bid):
    card_numbers = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    if "J" in hand:
        j_count = hand.count("J")
        modified_hand = hand.replace("J", "")
        reference_rank = identify_hand(modified_hand, bid, card_numbers).rank

        if reference_rank == 1:
            return Hand(0, bid, [card_numbers.index(card) for card in [char for char in hand]])
        elif reference_rank == 3:
            if j_count == 2:
                return Hand(0, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif j_count == 1:
                return Hand(1, bid, [card_numbers.index(card) for card in [char for char in hand]])
        elif reference_rank == 4:
            return Hand(2, bid, [card_numbers.index(card) for card in [char for char in hand]])
        elif reference_rank == 5:
            if j_count == 3:
                return Hand(0, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif j_count == 2:
                return Hand(1, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif j_count == 1:
                return Hand(3, bid, [card_numbers.index(card) for card in [char for char in hand]])
        elif reference_rank == 6:
            if j_count == 4:
                return Hand(0, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif j_count == 3:
                return Hand(1, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif j_count == 2:
                return Hand(3, bid, [card_numbers.index(card) for card in [char for char in hand]])
            elif j_count == 1:
                return Hand(5, bid, [card_numbers.index(card) for card in [char for char in hand]])
        return Hand(0, bid, [card_numbers.index(card) for card in [char for char in hand]])
    else:
        return(identify_hand(hand, bid, card_numbers))

def order_hands(hands):
    i = 1
    while i < len(hands):
        if i <= 0:
            i += 1
            continue
        if (hands[i].rank < hands[i-1].rank):
            temp = hands[i]
            hands[i] = hands[i-1]
            hands[i-1] = temp
            i -= 2
        elif (hands[i].rank == hands[i-1].rank):
            for j in range(5):
                if hands[i].cards[j] < hands[i-1].cards[j]:
                    temp = hands[i]
                    hands[i] = hands[i-1]
                    hands[i-1] = temp
                    i -= 2
                elif hands[i].cards[j] > hands[i-1].cards[j]:
                    break
        i += 1







main()
