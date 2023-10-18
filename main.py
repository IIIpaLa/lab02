def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    prime_numbers = []
    for i in range(2, n + 1):
        if primes[i]:
            prime_numbers.append(i)

    return prime_numbers


# Пример использования
n = 30
print(sieve_of_eratosthenes(n))  # Выводит [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
