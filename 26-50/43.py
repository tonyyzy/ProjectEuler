from itertools import permutations

a_list = list(permutations(range(0, 10), 10))
number_list = []
prime_list = [0, 2, 3, 5, 7, 11, 13, 17]
result = 0
for i in a_list:
    b = ""
    while True:
        k = 1
        while k < 8:
            if int(str(i[k]) + str(i[k + 1]) + str(i[k + 2])) % prime_list[k] != 0:
                break
            else:
                k += 1
        if k != 8:
            break
        else:
            for j in i:
                b += str(j)
            result += int(b)
            break

print(result)
