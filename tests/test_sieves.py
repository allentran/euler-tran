import unittest

import numpy as np
import numpy.testing
from euler_tran.prime.sieves import Erasosthenes, PrimalityTest
from euler_tran.prime import factors


class SieveTests(unittest.TestCase):

    def erastosthenes_test(self):
        primes = Erasosthenes.primes_less_than(12, return_set=False)
        numpy.testing.assert_array_equal(np.array([2, 3, 5, 7, 11]), primes)

    def test_is_prime(self):
        tester = PrimalityTest()
        self.assertTrue(tester.is_prime(349))

    def test_factors(self):
        f = factors.PrimeFactors()
        x = f.get_factors(22)
        self.assertEquals(x, [2, 11])
        x = f.get_factors(75)
        self.assertEquals(x, [3, 5])
