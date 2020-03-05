from euler import *


def prime_factors(num):
    a = factorise(num)
    a = set(a)
    return len(a)

s = 100000
counter = 0
while counter < 4:
    if prime_factors(s) == 4:
        counter += 1
        s += 1
    else:
        counter = 0
        s += 1

print(s - 4)
