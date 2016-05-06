import itertools


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1



print(list(itertools.takewhile(lambda x : x <= 31, primes())))