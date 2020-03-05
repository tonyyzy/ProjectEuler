from decimal import getcontext, Decimal

getcontext().prec = 102

non_natural = []

for i in range(1, 101):
    if i ** 0.5 % 1 != 0:
        non_natural.append(i)

result = 0
for i in non_natural:
    a = Decimal(i).sqrt()
    result += sum(int(c) for c in str(a * (10 ** 99))[:100])

print(result)