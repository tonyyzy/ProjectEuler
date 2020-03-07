def s(n):
    if n < 10:
        return n
    else:
        reminder = n % 9
        val = int(n/9)
        return int(str(reminder) + val * "9") % 1000000007

def S(k):
    n = k // 9
    mod = k % 9
    total = int("1" * n)


def fibo(x):
    l = [0, 1]
    while len(l) < x+1:
        l.append(l[-1] + l[-2])
    return l

if __name__ == "__main__":
    print(fibo(90))
    # total = 0
    # # for i in range(2, 91):
    # #     total += S(seq[i])
    # #     if total > 1000000007:
    # #         total %= 1000000007
    # # print(total % 1000000007)
    # print(seq[-1])
    # x = S(seq[5])
    # print(len(x), x[-1])
    # x = []
    # for i in range(100000):
    #     x.append(s(i))
    # print(len(x), len(set(x)))
    # for i in x:
    #     if x.count(i) != 1:
    #         print(i)
    # largest fibo: 2880067194370816120