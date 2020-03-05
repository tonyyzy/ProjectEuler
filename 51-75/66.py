D = []
for i in range(2, 1001):
    if i ** 0.5 % 1 != 0:
        D.append(i)
#
# result = 0
# for i in D:
#     n = 70000
#     while True:
#         if ((n ** 2 - 1) / i) ** 0.5 % 1 == 0:
#             print(i, n)
#             break
#         else:
#             n += 1

# Chakravala method
# result = []
# n = 61
# root = int(n ** 0.5)
# b = 1
# a = int(n ** 0.5)
# c = abs(a ** 2 - n * (b ** 2))
# while c != 1:
#     init = c - (a % c)
#     k = 0
#     while ((init + k * c) / b) % 1 != 0:
#         k += 1
#     con = int((init + k * c) / b)
#     m = (root - con) // c
#     mm = m * c + con
#     mm1 = (m + 1) * c + con
#     if mm > mm1:
#         m += 1
#     mm = m * c + con
#     a, b = int((a * mm + n * b) / c), int((a + b * mm) / c)
#     c = abs(int(a ** 2 - n * b ** 2))
#     print(a, b, c)
# print(a,b,c)
# too long for 211


total = [0, 0]
for num in D:
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
            break
        else:
            n += 1
    if denominator > total[0]:
        total = [denominator, num]

print(total)