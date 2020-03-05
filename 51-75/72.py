total = list(range(1000001))

for i in total[2:]:
    if total[i] == i:
        for j in range(i, 1000001, i):
            total[j] = total[j] // i * (i - 1)

print(sum(total) - 1)