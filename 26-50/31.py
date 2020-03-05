coins = [2, 5, 10, 20, 50, 100, 200]

result = [1] * 201

for i in coins:
    for j in range(i,201):
        result[j] += result[j - i]

print(result)
