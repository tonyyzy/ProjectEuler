sums = 1
for i in range(1, 501):
    a = i * 2 + 1
    b = i * 2
    sums += a ** 2 * 4 - 6 * b

print(sums)