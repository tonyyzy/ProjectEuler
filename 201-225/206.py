import re


if __name__ == "__main__":
    a = 101010103 # sqrt(10203040506070809)
    while re.match(r"1.2.3.4.5.6.7.8.9", str(a ** 2)) == None:
        if a % 10 == 3:
            a += 4
        else:
            a += 6

    print(a * 10)