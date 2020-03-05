import math
def check_prime(a):
    root = math.sqrt(a)
    root = math.floor(root)
    for i in range(2, root +1):
        if a%i == 0:
            return False
    return True

a = 0
for i in range(2, 2000001):
    if check_prime(i) == True:
        a += i
print(a)