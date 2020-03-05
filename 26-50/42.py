import string
from euler import *
from collections import OrderedDict

convert = OrderedDict()
for i in range(0, 26):
    convert[string.ascii_uppercase[i]] = i + 1

all_names = text_to_list("42.txt")


def check_triangle(word):
    a = 0
    for i in word:
        a += convert[i  ]
    b = math.floor(math.sqrt(a * 2))
    if a * 2 == b * (b + 1):
        return True
    else:
        return False

results = 0
for i in all_names:
    if check_triangle(i):
        results += 1

print(results)
