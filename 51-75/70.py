from euler import prime_sieve
from itertools import combinations_with_replacement as combinations

primes = reversed(list(prime_sieve(5000)))
result = [9, 0]
for i in combinations(primes, 2):
    if i[0] * i [1] < 10 ** 7 and sorted(list(str(i[0] * i[1]))) == sorted(list(str((i[0] - 1)*(i[1] - 1)))) and \
                                    (i[0] * i[1]) / ((i[0] - 1)*(i[1] - 1)) < result[0]:
        result = [(i[0] * i[1]) / ((i[0] - 1)*(i[1] - 1)), (i[0] * i[1])]

print(result)
