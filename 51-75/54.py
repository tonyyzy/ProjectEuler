player1 = []
player2 = []

with open("poker.txt") as hands:
    for i in hands:
        player1.append(i.split()[0:5])
        player2.append(i.split()[5:10])

conversion = {"A": 14,
              "J": 11,
              "Q": 12,
              "K": 13,
              "T": 10}

results = {1: "High card",
           2: "Pair",
           3: "Two pairs",
           4: "Three of a kind",
           5: "Straight",
           6: "Flush",
           7: "Full house",
           8: "Four of a kind",
           9: "Straight flush",
           10: "Royal flush"}

points = {}
values = list(range(2, 15))
for i in range(13):
    if values[i] < 10:
        points[values[i]] = "0" + str(values[i])
    else:
        points[values[i]] = str(values[i])


def check_straight(numbers):
    if numbers[0] + 4 == numbers[1] + 3 == numbers[2] + 2 == numbers[3] + 1 == numbers[4]:
        return True


def check_flush(units):
    if len(set(units)) == 1:
        return True


def check_same(numbers):
    k = list(numbers)
    count = len(set(numbers))
    if count == 4:
        mu = list(numbers)
        for x in set(numbers):
            mu.remove(x)
        k = list(set(numbers))
        k.sort()
        return float("2." + points[mu[0]] + points[k[-1]])
    elif count == 3:
        for x in set(numbers):
            k.remove(x)
        if len(set(k)) == 2:
            return 3
        else:
            return 4
    elif count == 2:
        mu = list(numbers)
        for x in set(numbers):
            mu.remove(x)
        if len(mu) == 1:
            return 8
        else:
            for x in set(numbers):
                k.remove(x)
                k.remove(x)
            return float("7." + points[k[0]])
    else:
        return float("1." + points[numbers[-1]])


def get_rank(numbers, units):
    if check_straight(numbers):
        if check_flush(units):
            if numbers[0] == 10:
                return 10
            else:
                return 9
        else:
            return 5
    elif check_flush(units):
        return 6
    else:
        return check_same(numbers)


class PlayCards:

    def __init__(self, cards):
        self.cards = cards

    def reorder(self):
        num_unit = []
        for card in self.cards:
            if card[0] in conversion.keys():
                num_unit.append([conversion[card[0]], card[1]])
            else:
                num_unit.append([int(card[0]), card[1]])
            num_unit.sort()
        numbers = []
        units = []
        for com in num_unit:
            numbers.append(com[0])
            units.append(com[1])
        return (numbers, units)

counter = 0
outing = []
for i in range(1000):
    cards_1 = PlayCards(player1[i]).reorder()
    cards_2 = PlayCards(player2[i]).reorder()
    if get_rank(cards_1[0], cards_1[1]) > get_rank(cards_2[0], cards_2[1]):
        counter += 1
print(counter)