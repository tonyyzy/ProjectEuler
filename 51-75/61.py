from itertools import permutations
from collections import OrderedDict


def generator(a, n):
    results = []
    b = int(n * ((a - 2) * n + 4 - a) / 2)
    while b < 10000:
        results.append(b)
        n += 1
        b = int(n * ((a - 2) * n + 4 - a) / 2)
    return results

triangle = generator(3, 45)
square = generator(4, 32)
pentagonal = generator(5, 26)
hexagonal = generator(6, 23)
heptagonal = generator(7, 21)
octagonal = generator(8, 19)

all_list = {1: triangle,
            2: square,
            3: pentagonal,
            4: hexagonal,
            5: heptagonal,
            6: octagonal}


def get_head(alist):
    results = []
    for i in alist:
        results.append(str(i)[0:2])
    return results


def get_tail(alist):
    results = []
    for i in alist:
        results.append(str(i)[2:4])
    return results
# for k in permutations(range(1, 7), 6):
#     reduction = list(all_list[k[0]])
#     summation = []
#     for c in all_list[k[0]]:
#         summation.append([0, c])
#     for i in k[1:]:
#         x = get_head(all_list[i])
#         temp = []
#         for j in reduction:
#             if j != 0 and str(j)[2:4] in x:
#                 temp.append(all_list[i][x.index(str(j)[2:4])])
#                 summation[reduction.index(j)][1] += all_list[i][x.index(str(j)[2:4])]
#                 summation[reduction.index(j)][0] += 1
#             else:
#                 temp.append(0)
#         if len(set(temp)) == 1:
#             print(temp)
#         reduction = list(temp)
#     summation.sort(reverse=True)
#     if summation[0][0] == 5 and str(list(set(temp))[0])[2:4] in get_head(all_list[k[0]]):
#         print(summation[0][1])


# def check_next(alist):
#     a = list(all_list[alist[0]])
#     result = []
#     reduction = {}
#     reduction.fromkeys()
#     for i in range(1,6):
#         string_dict = {}
#         for count in all_list[alist[i]]:
#             if str(count)[0:2] in string_dict.keys():
#                 string_dict[str(count)[0:2]].append(count)
#             else:
#                 string_dict[str(count)[0:2]] = [count]
#         temp = []
#         ks = []
#         for k in a:
#             if str(k)[2:4] in string_dict.keys():
#                 ks.append(k)
#                 for x in string_dict[str(k)[2:4]]:
#                     temp.append(x)
#         result.append(ks)
#         a = list(set(temp))
#     if get_tail(a)[0] in get_head(result[0]):
#         return a
#     else:
#         return False
#     # return a
#
# # for i in permutations(range(1, 7), 6):
# #     a = check_next(i)
# #     if a != False:
# #         print(a)
# print(check_next([1, 2, 3, 4, 5, 6]))


def reduce(alist):
    result = OrderedDict()
    for i in range(1, 7):
        result[i] = all_list[alist[i - 1]]
    for j in range(0, 150):
        temp = []
        x = string_dict(result[(j + 1) % 6 + 1])
        for k in result[j % 6 + 1]:
            if str(k)[2:4] in x:
                temp.append(k)
        result[j % 6 + 1] = temp
    if len(result[1]) != 0:
        return result
    else:
        return False


def string_dict(alist):
    string = {}
    for i in alist:
        if str(i)[0:2] in string.keys():
            string[str(i)[0:2]].append(i)
        else:
            string[str(i)[0:2]] = [i]
    return string

for i in permutations(range(1, 7), 6):
    a = reduce(i)
    if a != False:
        print(a)
# print(reduce([1, 2, 3, 4, 5, 6]))
# # print(string_dict(triangle))