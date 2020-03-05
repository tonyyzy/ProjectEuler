# from math import floor
#
#
# def decom(x, y):
#     if y > x/2:
#         return 1
#     else:
#         counter = 1
#         for i in range(y, floor(x/2) + 1):
#             counter += chart[x - i - 1][i - 1]
#         return counter
#
# # a = 61
# # k = 1
# # while k != 0:
# #     print(a)
# #     if decom(a, 1) % 1000000 == 0:
# #         print(a)
# #         break
# #     else:
# #         a += 1
#
# # print(decom(4, 2))
#
# chart = [[1]]
# count = 2
# while chart[-1][0] % 1000000 != 0:
#     print(chart[-1][0])
#     temp = []
#     for i in range(1, count + 1):
#         temp.append(decom(count, i))
#     chart.append(temp)
#     count += 1

# list of generalized pentagonal numbers for generating function
k = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

p, sgn, n, m = [1], [1, 1, -1, -1], 0, 1e6

while p[n] > 0:    # expand generating function to calculate p(n)
    n += 1
    px, i = 0, 0
    while k[i] <= n:
        px += p[int(n - k[i])] * sgn[i % 4]
        i += 1
    p.append(px % m)

print("Project Euler 78 Solution =", n)

# Todo look into integer partition and generating function
