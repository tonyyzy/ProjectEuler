from euler import *
from itertools import combinations
from math import factorial

prime = prime_sieve(10000)[1:]


def check_concatenate(alist):
    a = len(alist)
    count = 0
    for j in combinations(alist, 2):
        if is_prime(int(str(j[0]) + str(j[1]))) and is_prime(int(str(j[1]) + str(j[0]))):
            count += 1
    if count == factorial(a) / (2 * factorial(a - 2)):
        return True
    else:
        return False


def sub_check(i):
    for j in prime[prime.index(i):]:
        if check_concatenate([i, j]):
            results = [i, j]
            n = prime.index(j)
            while len(results) < 5:
                a = list(results)
                a.append(prime[n])
                if check_concatenate(a):
                    results.append(prime[n])
                n += 1
                if n == len(prime):
                    break
            if len(results) == 5:
                return sum(results)
    return False

for i in prime:
    a = sub_check(i)
    if a != False:
        print(a)
        break

# result = []
# for i in combinations(prime, 5):
#     count = 0
#     c = i[0]
#     for j in combinations(i, 2):
#         if is_prime(int(str(j[0]) + str(j[1]))) and is_prime(int(str(j[1]) + str(j[0]))):
#             count += 1
#     if count == 10:
#         print(i)
#         break
