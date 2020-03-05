from euler import *

n = 137
a = 135
while True:
    if check_prime(n):
        a = n
        n += 2
    else:
        while check_prime(a):
            b = (n - a) / 2
            if math.sqrt(b) % 1 == 0:
                a = n
                n += 2
                break
            else:
                a -= 2
        if a == 1:
            print(n)
            break
        else:
            a -= 2


