from euler import factorise
from math import gcd

total = 0
for i in range(4, 12001):
    for j in range(i // 3 + 1, i // 2 + 1):
        if gcd(i, j) == 1:
            total += 1

print(total)

