numerator = 3
denominator = 2
total = 0
for i in range(1000):
    if len(str(numerator)) > len(str(denominator)):
        total += 1
    a = numerator + denominator
    b = numerator + denominator * 2
    numerator = b
    denominator = a

print(total)
