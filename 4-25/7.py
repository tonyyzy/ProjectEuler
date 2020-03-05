import math
def check_prime(a):
    root = math.sqrt(a)
    root = math.floor(root)
    for i in range(2, root +1):
        if a%i == 0:
            return False
    return True

a = 0
num = 2
while a != 10001:
    if check_prime(num) == True:
        num += 1
        a +=1
    else:
        num +=1

print(num-1)
