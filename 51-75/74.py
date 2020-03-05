from math import factorial as fac


def get_chain(num):
    chain = []
    n = 0
    while n not in chain:
        chain.append(n)
        n = 0
        for i in str(num):
            n += fac(int(i))
        num = n
    return len(chain)

total = 0

for i in range(1000001):
    if get_chain(i) == 60:
        total += 1

print(total)