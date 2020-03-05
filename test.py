from fractions import Fraction as f
n = 0
while True:
    result = []
    a0 = num ** 0.5 //1
    a = num ** 0.5 // 1
    d = 1
    m = 0
    result.append(int(a0))
    for i in range(n):
        m = a * d - m
        d = (num - m ** 2) / d
        a = ((a0 + m) / d) // 1
        result.append(int(a))

    numerator = 1
    denominator = result[-1]
    for i in list(reversed(result))[1:]:
        numerator += i * denominator
        denominator, numerator = numerator, denominator
    if denominator ** 2 - num * numerator ** 2 == 1:
        print(denominator)
        break
    else:
        n += 1