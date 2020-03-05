a = []

with open('p081_matrix.txt') as matrix:
    for i in matrix.readlines():
        b = []
        for j in i.split(','):
            b.append(int(j))
        a.append(b)

for i in range(80):
    for j in range(80):
        if i == 0 and j == 0:
            a[i][j] = a[i][j]
        elif i == 0:
            a[i][j] += a[i][j - 1]
        elif j == 0:
            a[i][j] += a[i - 1][j]
        else:
            if a[i - 1][j] > a[i][j - 1]:
                a[i][j] += a[i][j - 1]
            else:
                a[i][j] += a[i - 1][j]

print(a)