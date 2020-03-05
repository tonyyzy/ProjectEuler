def digits(num):
    a = []
    for i in str(num):
        a.append(int(i))
    a.sort()
    return a

mul = [6, 5, 4, 3, 2]
num = 10
n = 0
while n < 5:
    n = 0
    for i in mul:
        if digits(num * i) == digits(num):
            n += 1
        else:
            num += 1
            break

print(num)