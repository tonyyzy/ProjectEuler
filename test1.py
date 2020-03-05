from euler import is_prime


def prime_list(a, b):
    results = []
    for i in range(a, b):
        if is_prime(i):
            results.append(i)
    return results

prime_list(2, 1000000)