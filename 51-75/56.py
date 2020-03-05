def digit_sum(number):
    string = str(number)
    total = 0
    for i in string:
        total += int(i)
    return total

token = 0
for i in range(100):
    for j in range(100):
        a = digit_sum(i ** j)
        if a > token:
            token = a

print(token)
