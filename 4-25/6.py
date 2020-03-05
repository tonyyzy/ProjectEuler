sum = 0
sqsum = 0
for i in range(1, 101):
    sqsum += i**2
    sum += i

print(sum**2 - sqsum)