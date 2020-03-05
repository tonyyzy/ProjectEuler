from collections import OrderedDict

result = OrderedDict()

with open("3") as text:
    for j in text.readlines():
        for i in j:
            if i in result:
                result[i] += 1
            else:
                result[i] = 1

print(result)