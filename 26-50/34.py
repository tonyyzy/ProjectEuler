import math

results = []
for i in range(3, 2540261):
    counter = 0
    for j in str(i):
        counter += math.factorial(int(j))
    if counter == i:
        results.append(i)

print(results)
