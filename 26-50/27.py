import math


def check_prime(a):
    root = math.sqrt(a)
    root = math.floor(root)
    for i in range(2, root + 1):
        if a % i == 0:
            return False
    return True

results = [0, 0, 0]
for i in range(-999, 100):
    for j in range(-999, 1000):
        n = 0
        temp = n ** 2 + i * n + j
        while temp > 0 and check_prime(temp):
            n += 1
            temp = n ** 2 + i * n + j
        if n > results[0]:
            results = [n, i, j]

print(results)

