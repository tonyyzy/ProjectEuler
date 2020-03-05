from euler import *


def reverse(number):
    string = str(number)
    return int(string[::-1])

total = 0
for i in range(10, 10000):
    counter = 1
    number = int(i)
    number += reverse(number)
    while counter < 51:
        if check_palindromic(str(number)):
            break
        else:
            counter += 1
            number += reverse(number)
    if counter == 51:
        total += 1

print(total)