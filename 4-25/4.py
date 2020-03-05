import math
a = []
list = []
for i in range(100, 1000):
    for j in range(i, 1000):
        num = i*j
        string = str(num)
        count = 0
        b = len(string)
        c = math.floor(b/2)
        if b > 1:
            for k in range(0, c):
                if string[k] == string[b - k- 1]:
                    count += 1
            if count == c:
                a.append([num,i,j])

a.sort()
print(a)