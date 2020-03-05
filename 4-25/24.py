import itertools

a = range(0,10)
b = list(itertools.permutations(a, 10))
print(b[999999])