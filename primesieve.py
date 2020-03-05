def primesieve(start, end):
    prime = []
    for x in range(1, end + 1, 2):
        prime.append(x)

    l = len(prime)
    for i in range(1, (l//2 + 1)):
        if prime[i] != 0:
            a = i + prime[i]
            while a < l:
                prime[a] = 0
                a += prime[i]

    prime1 = []
    for i in prime[1:]:
        if i >= start:
            prime1.append(i)
    if start <=2:
        prime1.insert(0, 2)
    return prime1

