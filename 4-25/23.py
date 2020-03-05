import math
import numpy as np

def sum_divisors(num):

    root = math.sqrt(num)
    a = 1
    if root % 1 == 0:
        root = int(root)
        a += root
        for j in range(2, root):
            if num % j == 0:
                a += j
                a += num / j
        return int(a)
    else:
        root = math.floor(root)
        for j in range(2, root + 1):
            if num % j == 0:
                a += j
                a += num / j
        return int(a)

list_abundant = []
for i in range(12, 28123):
    if sum_divisors(i) > i:
        list_abundant.append(i)

list_sum = list(range(1, 28124))
a_list = []
for i in range(0, len(list_abundant)):
    for j in range(i, len(list_abundant)):
        a_list.append(list_abundant[i] + list_abundant[j])

b_list = set(a_list)
total = list(set(list_sum) - b_list)
total.sort()
print(sum(total))
