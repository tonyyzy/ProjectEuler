a = 1
b = 1
c = 0
d = 2
while True:
    c = a + b
    d += 1
    if len(str(c)) == 1000:
        print(d)
        break
    a = b
    b = c

