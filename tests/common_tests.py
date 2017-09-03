import unittest

import numpy as np

from euler_tran.sequence import product
from euler_tran.divisors import factors


class CommonMethodTests(unittest.TestCase):

    def find_factors_test(self):
        self.assertEqual(factors.factors_of_n(6), {1, 2, 3, 6})
        self.assertEqual(factors.factors_of_n(1), {1})

    def largest_product_test(self):

        self.assertEqual(product.largest_product_in_list(
            [1, 2, 3, 0, 1, 1, 1, 1]), (1, [1, 1, 1, 1])
        )
        self.assertEqual(product.largest_product_in_list([1, 2, 3, 1, 1, 1, 1, 1]), (6, [1, 2, 3, 1]))
        self.assertEqual(product.largest_product_in_list([1, 2, 3, 1, 1, 7, 1, 1], n=2), (7, [1, 7]))
