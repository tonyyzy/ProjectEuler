def check_pandigit(num):
    a = []
    string = str(num)
    for i in string:
        a.append(int(i))
    a.sort()
    if a == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return True
    else:
        return False

results = []
for i in range(1, 10000):
    n = 1
    length = 0
    b = ""
    while length <= 9:
        a = i * n
        b += str(a)
        length = len(b)
        if length == 9:
            if check_pandigit(b):
                results.append(int(b))
            else:
                break
        n += 1
results.sort(reverse=True)
print(results)