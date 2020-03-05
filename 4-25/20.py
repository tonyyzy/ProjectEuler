factorial = 1
for i in range(1, 101):
    factorial *= i

sum1 = 0

for i in str(factorial):
    sum1 += int(i)

print(sum1)