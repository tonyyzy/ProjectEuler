from euler import *

results = {x: [0, 0, 0] for x in range(3, 1000, 2) if check_prime(x)}
for i in range(3, 1000, 2):
    if check_prime(i):
        a = i + 2
        n = 0
        total = 0
        while total < 1000000:
            if check_prime(total) == True and results[i][0] < n:
                results[i] = [n, i, total]
            if check_prime(a):
                total += a
                a += 2
                n += 1
            else:
                a += 2

results1 = []
for i in results:
    results1.append([results[i][0], results[i][2]])

results1.sort()
print(results1)