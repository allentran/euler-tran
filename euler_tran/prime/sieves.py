import numpy as np
from bitarray import bitarray


class PrimalityTest(object):
    def __init__(self, max_prime=200, use_set=False):
        if use_set:
            self.known_primes = Erasosthenes.primes_less_than(max_prime)
        else:
            self.known_primes = np.array(Erasosthenes.primes_less_than(max_prime, return_set=False))

    def is_prime_in_sieve(self, n):
        return n in self.known_primes

    def is_prime(self, n):
        sqrt_n = int(np.sqrt(n))
        valid_prime_factors = self.known_primes[self.known_primes < sqrt_n]
        n = abs(n)
        if n <= 1:
            return False
        elif n % 3 == 0:
            return False
        elif any([p < n and n % p == 0 for p in valid_prime_factors]):
            return False
        else:
            for i in range(5, sqrt_n):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
        return True


class Erasosthenes(object):

    @staticmethod
    def primes_less_than(x, return_set=True, return_bitarray=False):

        primes = bitarray(x)
        primes.setall(True)
        sqrt_n = int(x ** .5) + 1
        primes[0::2] = False
        primes[:2] = False
        primes[2] = True
        for p in range(3, sqrt_n + 1, 2):
            if primes[p]:
                primes[p * p::2 * p] = False

        if return_bitarray:
            return primes

        if return_set:
            ps = set()
        else:
            ps = []
        for idx in range(x):
            if primes[idx]:
                if return_set:
                    ps.add(idx)
                else:
                    ps.append(idx)
        return ps

