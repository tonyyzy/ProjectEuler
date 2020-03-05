from math import gcd, sqrt
#
# total = 0
# for i in range(1, 500000):
#     for j in range(i, 500000):
#         root = sqrt(i ** 2 + j ** 2)
#         if root % 1 == 0 and (root + i + j) <= 1500000:
#             total += 1
#
# print(total)

# Pythagorean Theorem, Euclid's method
con = 1500000
sqrt_con = int(sqrt(con)) + 1
total = [0] * (con + 1)
for m in range(1, sqrt_con):
    for n in range(1, m):
        if gcd(m, n) == 1 and (m - n) % 2 == 1:
            sum = 2 * m ** 2 + 2 * m * n
            for k in range(sum, con, sum):
                total[k] += 1


print(total.count(1))
