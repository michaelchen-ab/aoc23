import sys
import functools

file = open(sys.argv[1]).read().strip()
lines = file.split("\n")


def v(num: str):
    if num == "A":
        return 14
    if num == "K":
        return 13
    if num == "Q":
        return 12
    if num == "J":
        return 1
    if num == "T":
        return 10
    return int(num)


def hand_type(cards: str):
    joker_replace = max(
        cards, key=lambda c: (c != "J", cards.count(c), -cards.index(c))
    )
    new_cards = [joker_replace if c == "J" else c for c in cards]
    c = sorted(new_cards, key=lambda x: (new_cards.count(x), v(x)), reverse=True)
    s = [v(x) for x in cards]
    # five of a kind
    if c[0] == c[4]:
        return (7, *s)
    # four of a kind
    if c[0] == c[3]:
        return (6, *s)
    # full house
    if c[0] == c[2] and c[3] == c[4]:
        return (5, *s)
    # three of kind
    if c[0] == c[2]:
        return (4, *s)
    # two pair
    if c[0] == c[1] and c[2] == c[3]:
        return (3, *s)
    # pair
    if c[0] == c[1]:
        return (2, *s)
    # high card
    return (1, *s)


def cmp(a, b):
    a_power = hand_type(a)
    b_power = hand_type(b)
    if a_power > b_power:
        return 1
    if a_power < b_power:
        return -1
    raise Exception()


mapp = {}
hands = []
for line in lines:
    hand, bet = line.split()
    mapp[hand] = int(bet)
    hands.append(hand)

sorted_hands = sorted(hands, key=functools.cmp_to_key(cmp))
total = 0
for rank, hand in enumerate(sorted_hands, start=1):
    total += rank * mapp[hand]
print(total)
