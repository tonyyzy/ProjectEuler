from primesieve import primesieve
from euler import is_prime
import math


def decom(x, y):
    primes = primesieve(y, math.ceil(x / 2))
    if y > x / 2:
        if is_prime(x):
            return 1
        else:
            return 0
    elif y == x / 2 and is_prime(y):
        return 1
    else:
        counter = 0
        for i in primes:
            counter += decom(x - i, i)
        counter += decom(x, x)
        return counter


i = 1
a = 12
while i != 0:
    if decom(a, 2) >= 5000:
        print(a)
        i = 0
    else:
        a += 1

        # Todo implement array look-up
