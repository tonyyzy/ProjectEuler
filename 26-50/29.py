results = []
for i in range(2, 101):
    for j in range(2, 101):
        results.append(i ** j)

results = set(results)
results = list(results)
print(len(results))