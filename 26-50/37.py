from euler import *
#
# count = 0
# results = []
# a = 13
# while count < 12:
#     while True:
#         if check_prime(a):
#             b = list(str(a))
#             for i in range(0, len(b)):
#                 c = ""
#                 d = ""
#                 for j in range(i, len(b)):
#                     c += b[j]
#                     d += b[len(b) - j - 1]
#                     e = d[::-1]
#                 print(c, e)
#                 if check_prime(int(c)) and check_prime(int(e)) != True:
#                     a += 2
#                     break
# results.append(a)
# print(results)
# count += 1
# a +=2


def check_string(string):
    b = list(string)
    for i in range(1, len(b)):
        c = ""
        d = ""
        for j in range(i, len(b)):
            c += b[j]
            d += b[len(b) - j - 1]
            e = d[::-1]
        if check_prime(int(c)) != True or check_prime(int(e)) != True:
            return False
    return True

count = 0
a = 13
results = []
while True:
    if check_prime(a) and check_string(str(a)) == True:
        results.append(a)
        a += 2
        count += 1
        if count == 11:
            break
    else:
        a += 2

print(sum(results))