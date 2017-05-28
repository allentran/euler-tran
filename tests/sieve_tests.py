import unittest

from euler_tran.prime.sieves import Erasosthenes

class SieveTests(unittest.TestCase):

    def erastosthenes_test(self):
        primes = Erasosthenes.primes_less_than(13)
        self.assertEqual({2, 3, 5, 7, 11}, primes)
