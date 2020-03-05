a = []
b = []
with open('p082_matrix.txt') as matrix:
    for i in matrix.readlines():
        b = []
        for j in i.split(','):
            b.append(int(j))
        a.append(b)


for i in range(1, 80):  # column
    b = []
    for j in range(80):  # row
        c = []
        for t in range(80):  # start row
            if j == t:
                c.append(a[j][i - 1] + a[j][i])
            else:
                sum_a = 0
                # sum_a += a[j][i]
                sum_a += a[t][i - 1]
                for q in range(min(t, j), max(t, j) + 1):
                    sum_a += a[q][i]
                c.append(sum_a)
        b.append(min(c))
    print(b)

    for k in range(80):
        a[k][i] = b[k]


print(min(b))
