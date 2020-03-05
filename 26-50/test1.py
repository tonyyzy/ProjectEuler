
b_list = [2, 2, 2, 2, 2, 2, 5, 13, 5, 19, 2, 7, 7]
b_list.sort()
b_dict = {}
token = 0
counter = 0
for i in b_list:
    if token == 0:
        token = i
        counter += 1
    elif token == i:
        counter += 1
    else:
        b_dict[token] = counter
        token = i
        counter = 1

b_dict[token] = counter

print(b_dict)