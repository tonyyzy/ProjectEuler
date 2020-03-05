import numpy as np

# 9^2 * 7 = 567, so only need 1 to 567

n = 0
yes = []
no = [1]
temp = []
for i in range(2, 568):
    n = i
    temp = []
    temp.append(n)
    while n not in (1, 89):
        temp.append(n)
        a = n
        n = 0
        while a > 9:
            n += (a - int(a.__floordiv__(10) * 10))**2
            a = int(a.__floordiv__(10))
        n += a ** 2
    if n == 1:
        no += temp
    else:
        yes += temp


yes = set(sorted(yes))

counter = 0
for i in range(2, 10000000):
    if i%1000 ==0:
        print(i)
    a = i
    n = 0
    while a > 9:
        n += (a - int(a.__floordiv__(10) * 10)) ** 2
        a = int(a.__floordiv__(10))
    n += a ** 2
    if n in yes:
        counter += 1

print(counter)