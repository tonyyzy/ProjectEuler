from euler import *

n = 144
while True:
    a = n * ( 2 * n - 1)
    if check_penta(a) and check_triangle(a) == True:
        print(a)
        break
    else:
        n += 1