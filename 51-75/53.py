from math import factorial


def combinatorial(n, r):
    return int((factorial(n))/(factorial(r) * factorial(n - r)))

count = 0
for i in range(23, 101):
    for j in range(1, i + 1):
        if combinatorial(i, j) > 1000000:
            count += 1

print(count)