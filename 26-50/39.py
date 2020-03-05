import math
from operator import itemgetter

results = {}

for i in range(1, 1001):
    results[i] = 0

for i in range(1, 500):
    for j in range(i, 500):
        a = math.sqrt(i ** 2 + j ** 2)
        b = i + j + a
        if a % 1 == 0 and b <= 1000:
            results[int(b)] += 1
results = sorted(results.items(), key=itemgetter(1), reverse=True)
print(results)

