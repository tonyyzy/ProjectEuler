normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 2
count = 0
for i in range(1901, 2001):
    if i % 4 == 0:
        for j in leap:
            if j % 7 + day == 7:
                count += 1
            day += j % 7
            if day > 7:
                day %= 7
    else:
        for j in normal:
            if j % 7 + day == 7:
                count += 1
            day += j % 7
            if day > 7:
                day %= 7
print(count)
