big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
small = "abcdefghijklmnopqrstuvwxyz"

result = 0
with open("4") as text:
    for i in text.readlines():
        for j in range(len(i)-8):
            if i[j] in small and i[j + 1] in big and i[j + 2] in big and i[j + 3] in big and i[j + 4] in small and i[j + 5] in big and i[j + 6] in big and i[j + 7] in big and i[j + 8] in small:
                print(i[j + 4])
