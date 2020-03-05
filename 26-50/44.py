import math


def check_penta(num):
    a = math.floor(math.sqrt(num * 2 / 3)) + 1
    if num == a * (3 * a - 1) / 2:
        return True
    else:
        return False


for i in range(1, 10000):
    for j in range(i, 10000):
        a = j * (3 * j - 1) / 2
        b = i * (3 * i - 1) / 2
        if check_penta(a - b) and check_penta(b + a):
            print(int(a - b))

