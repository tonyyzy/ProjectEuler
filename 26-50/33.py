from euler import *
import math


results = []
for i in range(1, 10):
    for j in range(0, 10):
        for k in range(1, 10):
            if j != k and j < k:
                if j / k == (j * 10 + i) / (k + i * 10):
                    results.append([(j * 10 + i), (k + i * 10)])
                elif j / k == (j + i * 10) / (k * 10 + i):
                    results.append([(j + i * 10), (k * 10 + i)])

numerator = []
denominator = []
for i in results:
    numerator.append(i[0])
    denominator.append(i[1])

a_list = []
for i in numerator:
    fac = []
    for j in factorise(i):
        a_list.append(j)

b_list = []
for i in denominator:
    fac = []
    for j in factorise(i):
        b_list.append(j)

a_list.sort()
b_list.sort()

a_dict = {}
token = 0
counter = 0
for i in a_list:
    if token == 0:
        token = i
        counter += 1
    elif token == i:
        counter += 1
    else:
        a_dict[token] = counter
        token = i
        counter = 1
a_dict[token] = counter

b_dict = {}
token = 0
counter = 0
for i in b_list:
    if token == 0:
        token = i
        counter += 1
    elif token == i:
        counter += 1
    else:
        b_dict[token] = counter
        token = i
        counter = 1

b_dict[token] = counter

c_dict = b_dict
# compare dicts, find least common denominator
for i in a_dict:
    if b_dict[i] >= a_dict[i]:
        c_dict[i] = b_dict[i] - a_dict[i]

final = 1
for i in c_dict:
    final *= i ** c_dict[i]

print(c_dict, final)
