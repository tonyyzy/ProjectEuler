import numpy as np
b, e = [],[]
with open("base_exp.txt") as file:
    for line in file:
        base, exp = line.split(',')
        b.append(int(base))
        e.append(int(exp))

b = np.array(b)
e = np.array(e) / 100000
arr = np.power(b, e)
# for i in range(1):
#     arr.append(b[i] ** e[i])
print(b)
print(e)
print(arr.argmax())
print(b[708])