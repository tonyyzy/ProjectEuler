def get_digit(num):
    root = num ** 0.5
    if root % 1 == 0:
        return
    counting = []
    b =  (root // 1)
    c = 1
    while True:
        d = (c / (root - b)) // 1
        e = num - b ** 2
        if e % c == 0:
            c = e / c
        else:
            c = e
        b =  (c * d - b)
        if [b, c] in counting:
            return counting
        else:
            counting.append([b, c])

result = 0
for i in range(10001):
    token = get_digit(i)
    if token != None and len(token) % 2 == 1:
        result += 1

print(result)