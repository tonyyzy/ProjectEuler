from itertools import permutations
from euler import *

for k in range(9, 0, -1):
    a = list(permutations(range(k, 0, -1), k))
    for i in a:
        b = ""
        for j in i:
            b += str(j)
        if check_prime(int(b)):
            print(b)
            break
