from euler import factorise, is_prime, prime_sieve
#
#
# def sieve(num, prime):
#     if prime == []:
#         return len(range(1, num))
#     result= list(range(num))
#     prime = set(prime)
#     for i in prime:
#         for k in range(1, int(num / i)):
#             result[k * i] = 0
#     result = set(result)
#     return len(result) - 1
#
# result = 0
# counter = 0
# for i in range(2, 1000000):
#     if not is_prime(i):
#         a = i / sieve(i, list(factorise(i)))
#         if  a > counter:
#             print(i)
#             counter = a
#             result = i
total = 1
for i in prime_sieve(2000):
    total *= i
    if total > 10 ** 7:
        print(total / i)
        break
