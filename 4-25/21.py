import math

result = []
for i in range(2,10001):
    root = math.sqrt(i)
    a = 1
    if root % 1 == 0:
        root = int(root)
        a += root
        for j in range(2, root):
            if i % j == 0:
                a += j
                a += i / j
        if i != a:
            result.append([i, int(a)])
    else:
        root = math.floor(root)
        for j in range(2, root + 1):
            if i % j == 0:
                a += j
                a += i / j
        if i != a:
            result.append([i, int(a)])

amicable = []
for i in range(0, len(result) - 1):
    for j in range(i, len(result)):
        if result[i][0] == result[j][1] and result[i][1] == result[j][0]:
            amicable.append(result[i])
            # amicable.append(result[j])
            break

print(amicable)

sum1 = 0
for i in amicable:
    sum1 += i[0] + i[1]

print(sum1)