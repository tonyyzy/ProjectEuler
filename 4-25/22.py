alpha_convert = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}
list_name = []
with open("22.txt") as names:
    list_name = list(names)

big_string = list_name[0]
a_list = big_string.split(",")
list_name = []
for i in a_list:
    list_name.append(i[1:-1])

list_name.sort()

total = 0
for i in list_name:
    token = 0
    for j in i:
        token += alpha_convert[j]
    total += token * (list_name.index(i) +1 )
print(total)

