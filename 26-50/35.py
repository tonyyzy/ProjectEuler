from euler import *
import timeit

start = timeit.default_timer()

results = [2]
for i in range(3, 1000000, 2):
    while check_prime(i):
        a = list(str(i))
        c = True
        for k in range(1, len(a)):
            b = ''
            for m in range(0, len(a)):
                b += a[(k + m) % len(a)]
            c = c and check_prime(int(b))
        while c:
            results.append(i)
            break
        break

print(len(results))

stop = timeit.default_timer()
print(stop - start)
