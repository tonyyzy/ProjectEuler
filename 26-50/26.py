def longest_repeat(num):
    remainder = 1
    a_list = []
    counter = 0
    while remainder*10 not in a_list:
        a_list.append(remainder * 10)
        remainder = (remainder * 10) % num
        counter += 1
    return counter

result = [0, 0]
for i in range(7, 1000):
    a = longest_repeat(i)
    if a > result[0]:
        result = [a, i]

print(result)
