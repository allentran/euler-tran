from functools import lru_cache

from .sieves import Erasosthenes


class PrimeFactors(object):

    def __init__(self):
        self.primes = Erasosthenes.primes_less_than(100, return_set=False)
        self.prime_set = set(self.primes)
        self.n = 100

    def _double(self):
        self.primes = Erasosthenes.primes_less_than(2 * self.n, return_set=False)
        self.prime_set = set(self.primes)
        self.n *= 2

    @lru_cache()
    def get_factors(self, n):
        if n > self.primes[-1]:
            self._double()

        if n in self.prime_set:
            return [n]

        factors = []
        for p in self.primes:
            if n == 1:
                return factors
            if n % p == 0:
                factors.append(p)
                while n > 1 and n % p == 0:
                    n /= p

                if n == 1:
                    return factors
                else:
                    return factors + self.get_factors(n)

