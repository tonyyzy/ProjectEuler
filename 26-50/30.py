n = 10
result = []
while n < 1000000:
    a = str(n)
    temp = 0
    for i in a:
        temp += int(i) ** 5
    if temp == n:
        result.append(n)
    n += 1

print(sum(result))
