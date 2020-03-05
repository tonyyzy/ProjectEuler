with open("18.txt") as raw_triangle:
    list_triangle = list(raw_triangle)

# remove \n
for i in range(len(list_triangle)-1):
    list_triangle[i] = list_triangle[i][:-1]

list_list = []
# string to list
for i in list_triangle:
    token = []
    for j in range(0, int((len(i)+1)/3)):
        token.append(int(i.split()[j]))
    list_list.append(token)

for i in range(1,15):
    token = []
    token.append(list_list[i][0] + list_list[i-1][0])
    for j in range(1, len(list_list[i])-1):
        if (list_list[i][j] + list_list[i-1][j-1]) >= (list_list[i][j] + list_list[i-1][j]):
            token.append(list_list[i][j] + list_list[i-1][j-1])
        else:
            token.append(list_list[i][j] + list_list[i-1][j])
    token.append(list_list[i][-1] + list_list[i-1][-1])
    list_list[i] = token
list_list[-1].sort()
print(list_list)

