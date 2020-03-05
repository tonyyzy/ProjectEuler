import math
for i in range(10, 1001):
    for j in range(10, 1001):
        if math.sqrt(i**2 + j**2) % 1 == 0 and math.floor(i + j + math.sqrt(i**2 + j**2)) == 1000:
            print(i*j*math.sqrt(i**2 + j**2))