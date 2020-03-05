coins = list(range(2, 100))

result = [1] * 101

for i in coins:
    for j in range(i, 101):
        result[j] += result[j - i]

print(result[-1])