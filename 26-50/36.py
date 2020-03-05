import math


def check_palindromic(string):
    a = list(string)
    b = len(a)
    leng = 0
    while leng < math.floor(b / 2) and a[leng] == a[-(1 + leng)]:
        leng += 1
    if leng == math.floor(b / 2):
        return True
    else:
        return False

sum1 = 0
for i in range(1, 1000000):
    if check_palindromic(str(i)) and check_palindromic(bin(i)[2:]) == True:
        sum1 += i

print(sum1)