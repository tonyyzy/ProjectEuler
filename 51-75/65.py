e = [2]
n = 1
while len(e) < 100:
    e += [1, 2 * n, 1]
    n += 1

e = list(reversed(e))

numerator = 1
denominator = e[0]
for i in e[1:]:
    numerator += denominator * i
    numerator, denominator = denominator, numerator

numerator, denominator = denominator, numerator
print(numerator, denominator)
result = 0
for i in str(numerator):
    result += int(i)

print(result)