import re
a = 100000000
while re.match(r"1.2.3.4.5.6.7.8.9", str(a ** 2)) == None:
    a += 1
    if a% 1000 == 0:
        print(a)

print(a)