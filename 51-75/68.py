from itertools import permutations


def check_equal(alist):
    for i in [1, 3, 5, 7, 9]:
        if alist[i - 1] == alist[i]:
            return False
    for i in [1, 3, 5, 7]:
        if alist[i] != alist[i + 1]:
            return False
    if alist[0] != alist[9]:
        return False
    return True


def check_sum(a, j):
    if 6 + a[0] + a[1] == j[0] + a[2] + a[3] == j[1] + a[4] + a[5] == j[2] + a[6] + a[7] == j[3] + a[8] + a[9]:
        return True
    else:
        return False

result = []
for j in permutations([7, 8, 9, 10], 4):
    for i in permutations([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 10):
        if check_equal(i) and check_sum(i, j):
            result.append(int('6' + str(i[0]) + str(i[1]) + str(j[0]) + str(i[2]) + str(i[3]) + str(j[1]) + str(i[4]) +
                              str(i[5]) + str(j[2]) + str(i[6]) + str(i[7]) + str(j[3]) + str(i[8]) + str(i[9])))


print(sorted(list(set(result))))


