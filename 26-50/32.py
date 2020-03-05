results = []
for i in range(1, 3000):
    for j in range(1, 3000):
        a = i * j
        b = str(i) + str(j) + str(a)
        c = []
        for k in b:
            c.append(int(k))
        c.sort()
        if c == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            results.append(a)

results = set(results)
print(sum(results))
