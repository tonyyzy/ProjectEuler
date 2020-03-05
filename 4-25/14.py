numbers = []
for i in range(1, 1000000):
    token = 0
    a = i
    while a != 1:
        if a % 2 == 0:
            a /= 2
            token += 1
        else:
            a = a*3 + 1
            token += 1
    numbers.append([token+1, i])

numbers.sort(reverse=True)
print(numbers[0])