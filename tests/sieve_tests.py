import unittest

import numpy as np
import numpy.testing
from euler_tran.prime.sieves import Erasosthenes, PrimalityTest


class SieveTests(unittest.TestCase):

    def erastosthenes_test(self):
        primes = Erasosthenes.primes_less_than(12)
        numpy.testing.assert_array_equal(np.array([2, 3, 5, 7, 11]), primes)

    def is_prime_test(self):
        tester = PrimalityTest()
        self.assertTrue(tester.is_prime(349))
