
a = 1
n = 1
k = 1
result = 1
while True:
    if k == 10000000:
        break
    else:
        if n >= k:
            result *= int(str(a)[-(n - k + 1)])
            print(a, n, k)
            a += 1
            n += len(str(a))
            k *= 10
        else:
            a += 1
            n += len(str(a))

print(result)