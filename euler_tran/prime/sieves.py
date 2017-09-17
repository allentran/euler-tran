import numpy as np
from bitarray import bitarray


class PrimalityTest(object):
    def __init__(self, max_prime=200, use_set=False):
        if use_set:
            self.known_primes = set(Erasosthenes.primes_less_than(max_prime))
        else:
            self.known_primes = np.array(Erasosthenes.primes_less_than(max_prime))

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
            for i in xrange(5, sqrt_n):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
        return True


class Erasosthenes(object):

    @staticmethod
    def primes_less_than(x):

        primes = bitarray(x)
        primes.setall(True)
        sqrt_n = int(x ** .5) + 1
        primes[0::2] = False
        primes[:2] = False
        primes[2] = True
        for p in xrange(3, sqrt_n + 1, 2):
            if primes[p]:
                primes[p * p::2 * p] = False

        ps = set()
        for idx in xrange(x):
            if primes[idx]:
                ps.add(idx)
        return ps
        return primes.nonzero()[0]

