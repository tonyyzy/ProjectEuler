import math
fac = []

def factorise(int):
    while int != 1:
        int = divide(int)
    return fac

def divide(num):
    for i in range(2, num + 1):
        if check_prime(i) == True and num%i == 0:
            fac.append(i)
            return int(num/i)


def check_prime(a):
    root = math.sqrt(a)
    root = math.floor(root)
    for i in range(2, root +1):
        if a%i == 0:
            return False
    return True

def lcm(a):
    total = []
    for i in range(2, a + 1):
        global fac
        fac = []
        total.append(factorise(i))
    occ = numbercount(a, total)
    su = 1
    for i in occ:
        su *= i[0] ** i[1]
    return su

def numbercount(tot, list):
    occ = []
    prime = []
    for i in range(2, tot +1):
        if check_prime(i) == True:
            prime.append(i)
            occ.append([i, 0])
    for i in range(2, tot+1):
        for j in prime:
            token = 0
            for k in range(0,len(list[i-2])):
                if list[i-2][k-1] == j:
                    token +=1
            if token > occ[prime.index(j)][1]:
                occ[prime.index(j)][1] = token
    return occ

# print(lcm(20))
print(factorise(90))