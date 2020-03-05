import timeit
from euler import *

start = timeit.default_timer()


def factorise1(int1):
    fac = []
    while int1 != 1:
        for i in range(2, int1 + 1):
            if check_prime(i) == True and int1 % i == 0:
                fac.append(i)
                int1 = int(int1 / i)
                break
    return fac

print(factorise(126782417))
stop = timeit.default_timer()
print(stop - start)
