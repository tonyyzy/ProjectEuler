from euler import *
results = []
for num in range(100001, 200000, 2):
    if check_prime(num):
        a = num
        b = str(a)
        for i in range(0, len(b) - 2):
            for j in range(i + 1, len(b) - 1):
                for q in range(j + 1, len(b)):
                    c = list(b)
                    n = 0
                    p = []
                    for k in range(0, 10):
                        c[i], c[j], c[q] = str(k), str(k), str(k)
                        d = ""
                        for m in c:
                            d += m
                        if len(str(int(d))) == len(str(a)) and check_prime(int(d)):
                            n += 1
                            p.append(int(d))
                    if n == 8:
                        results.append(p)
print(results)
