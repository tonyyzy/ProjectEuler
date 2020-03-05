from euler import *

ratio = 1
n = 1
num_prime = 0
num_total = 1
temp_list = []
while ratio > 0.1:
    n += 1
    a = (2 * n - 1) ** 2
    b = 2 * (n - 1)
    temp_list = [a, a - b, a - 2 * b, a - 3 * b]
    for i in temp_list:
        if check_prime(i):
            num_prime += 1
    num_total += 4
    ratio = num_prime / num_total

print(2 * n - 1)