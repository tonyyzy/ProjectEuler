import math

from bisect import bisect_left


def prime_sieve(num):
    natural = list(range(3, num, 2))
    c = len(natural)
    for i in range(int((c / 2) ** .5)):
        if natural[i] != 0:
            n = 0
            a = natural[i]
            while a + n * a + i < c:
                natural[a + n * a + i] = 0
                n += 1
    natural = list(set(natural))
    natural.sort()
    natural[0] = 2
    return natural


# sqrt(1000000000) = 31622
__primes = prime_sieve(31622)


def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= 31622:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    # fall back on trial division if n > 1 billion
    for f in range(31627, limit, 6): # 31627 is the next prime
        if n % f == 0 or n % (f + 4) == 0:
            return False
    return True


def factorise(int1):
    fac = []
    while int1 % 2 == 0:
        fac.append(2)
        int1 = int(int1 / 2)
    start = 3
    while int1 != 1:
        for i in range(start, int1 + 1, 2):
            if is_prime(i) == True and int1 % i == 0:
                while int1 % i == 0:
                    fac.append(i)
                    int1 = int(int1 / i)
                break
        start = fac[-1] + 2
    return fac


def check_prime(a):
    if a == 1:
        return False
    root = int(a ** .5)
    for i in range(2, root + 1):
        if a % i == 0:
            return False
    return True


def check_pandigit(num):
    a = []
    string = str(num)
    for i in string:
        a.append(int(i))
    a.sort()
    if a == list(range(1, len(str(num)) + 1)):
        return True
    else:
        return False


def text_to_list(names_file):
    with open(names_file) as names:
        big_string = names.read()
    a_list = big_string.split(",")
    list_name = []
    for i in a_list:
        list_name.append(i[1:-1])
    return list_name


def check_penta(num):
    a = math.floor(math.sqrt(num * 2 / 3)) + 1
    if num == a * (3 * a - 1) / 2:
        return True
    else:
        return False


def check_triangle(num):
    b = math.floor(math.sqrt(num * 2))
    if num * 2 == b * (b + 1):
        return True
    else:
        return False


def check_palindromic(string):
    a = list(string)
    b = len(a)
    leng = 0
    while leng < math.floor(b / 2) and a[leng] == a[-(1 + leng)]:
        leng += 1
    if leng == math.floor(b / 2):
        return True
    else:
        return False