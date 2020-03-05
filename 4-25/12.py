import math

def number_divider(a):
    token = 0
    root = math.sqrt(a)
    if root % 1 == 0:
        root = int(root)
        for i in range(1, root):
            if a % i == 0:
                token += 2
        return token+1
    else:
        root = math.floor(root)
        for i in range(1, root):
            if a % i == 0:
                token += 2
        return token

q = 1
num = 1
while True:
    if number_divider(num) <= 500:
        q += 1
        num += q
    else:
        print(num)
        break
