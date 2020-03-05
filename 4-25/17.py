from num2words import num2words

a = 0
for i in range(1, 1001):
    string = num2words(i)
    string = string.replace("-","")
    string = string.replace(" ","")
    a += len(string)

print(a)

