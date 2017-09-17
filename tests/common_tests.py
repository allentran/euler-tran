import unittest

from euler_tran.sequence import product, collatz, misc
from euler_tran.divisors import factors


class CommonMethodTests(unittest.TestCase):

    def fib_test(self):
        gen = misc.fibonacci_generator()
        for _ in xrange(10):
            idx, val = gen.next()

        self.assertEqual(idx, 10)
        self.assertEqual(val, 55)

    def recurring_frac_test(self):
        self.assertEqual(misc.recurring_fraction(7), 6)
        self.assertEqual(misc.recurring_fraction(9), 1)
        self.assertEqual(misc.recurring_fraction(6), 1)

    def find_factors_test(self):
        self.assertEqual(factors.factors_of_n(6), {1, 2, 3, 6})
        self.assertEqual(factors.factors_of_n(1), {1})

    def largest_product_test(self):

        self.assertEqual(product.largest_product_in_list(
            [1, 2, 3, 0, 1, 1, 1, 1]), (1, [1, 1, 1, 1])
        )
        self.assertEqual(product.largest_product_in_list([1, 2, 3, 1, 1, 1, 1, 1]), (6, [1, 2, 3, 1]))
        self.assertEqual(product.largest_product_in_list([1, 2, 3, 1, 1, 7, 1, 1], n=2), (7, [1, 7]))

    def collatz_test(self):
        collatz_seqs = collatz.CollatzCache()
        self.assertEqual(collatz_seqs.until_n0(13), 10)

    def square_div_test(self):
        sq = misc.SquareDigitChain()
        end = sq.get_end(44, [44])
        self.assertEqual(end, 1)
        self.assertGreater(len(sq.str_cache), 1)

        end = sq.get_end(85, [85])
        self.assertEqual(end, 89)

        sq = misc.SquareDigitChain()
        ones = []
        for n in xrange(1, 14):
            end = sq.get_end(n, [n])
            if end == 1:
                ones.append(n)
        self.assertIn(13, ones)
        self.assertIn(7, ones)
