from itertools import permutations
from euler import *

total = []
for i in range(1001, 10000, 2):
    if check_prime(i):
        a = list(permutations(str(i), 4))
        b = []
        for j in a:
            c = ""
            for k in j:
                c += k
            b.append(int(c))
        b = set(b)
        b = list(b)
        b.sort()
        c = []
        for m in b:
            if check_prime(m) == True and len(str(m)) == 4:
                c.append(m)
        if len(c) >= 3 and c not in total:
            total.append(c)

for i in total:
    diff = []
    for j in range(0, len(i)):
        for k in range(j + 1, len(i)):
            if (2 * i[k] - i[j]) in i:
                print(i[j], i[k], 2 * i[k] - i[j])