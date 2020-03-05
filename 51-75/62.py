from collections import OrderedDict
# 345 ** 3 = 41063625
n = 465
cubic_dict = OrderedDict()
while True:
    a = n ** 3
    if a < 10000000000000:
        b = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        c = ""
        for i in str(a):
            b[int(i)] += 1
        for i in b:
            c += str(i)
        if c in cubic_dict.keys():
            cubic_dict[c][0] += 1
            cubic_dict[c][1].append(a)
        else:
            cubic_dict[c] = [1, [a]]
    else:
        break
    n += 1

for key in cubic_dict.keys():
    if cubic_dict[key][0] == 5:
        print(cubic_dict[key])