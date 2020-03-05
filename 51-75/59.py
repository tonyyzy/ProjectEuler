from itertools import product

string = ""
with open("cipher.txt") as cipher:
    string = cipher.readline()

string = string[:-1]
char = []
for i in string.split(sep=","):
    char.append(int(i))

keys = list(product("abcdefghijklmnopqrstuvwxyz", repeat=3))

deciphed = []
for i in keys:
    key = []
    decipher= []
    for j in range(1201):
        key.append(i[j % 3])
    count = 0
    words = ""
    sum1 = 0
    while count < 1201:
        a = char[count] ^ ord(key[count])
        if 30 < a < 123 and a != 96:
            words += chr(a)
            sum1 += a
            count += 1
        else:
            break
    if len(words) == 1201:
        deciphed.append([words, sum1])

print(deciphed)
