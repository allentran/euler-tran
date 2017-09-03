
import numpy as np

from euler_tran.prime import sieves
from euler_tran.sequence import product
from euler_tran.divisors import factors

class Problem(object):
    def get_answer(self):
        raise NotImplementedError


class Problem4(Problem):
    def __init__(self):

        self.min = 100
        self.max = 999

    def ispalindrome(self, num):

        str_num = str(num)
        return str_num == str_num[::-1]

    def max_palin(self):

        curr_max = 0
        for num_i in xrange(self.min, self.max + 1):
            for num_j in xrange(self.min, self.max + 1):
                product = num_i * num_j
                if product >= curr_max and self.ispalindrome(num_i * num_j):
                    curr_max = product
        return curr_max

    def get_answer(self):
        print self.max_palin()


class Problem5(Problem):
    def __init__(self):

        self.primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def find_prime_factors(self, num):
        factors = {}
        for prime in self.primes:
            curr_num = num
            if num % prime == 0:
                count = 0
                while curr_num % prime == 0:
                    count += 1
                    curr_num /= prime
                factors[prime] = count
        print factors
        return factors

    def find_smallest_prod(self, max_prod):

        prods = range(1, max_prod + 1)
        primes = {}
        for num in prods:
            factors = self.find_prime_factors(num)
            for f in factors:
                if f in primes:
                    if factors[f] > primes[f]:
                        primes[f] = factors[f]
                else:
                    primes[f] = factors[f]
        cum_prod = 1
        for f in primes:
            cum_prod *= f ** primes[f]

        return primes, cum_prod

    def get_answer(self):
        print self.find_smallest_prod(20)


class Problem6(Problem):
    def findSum(self, num):
        cum_squares = 0
        cum_sum = 0
        for ii in xrange(1, num + 1):
            cum_squares += ii ** 2
            cum_sum += ii
        return cum_sum ** 2 - cum_squares

    def get_answer(self):
        print self.findSum(100)


class Problem7(Problem):
    def get_prime_number(self, number=10001):

        def is_prime(candidate, primes):
            if candidate % 2 == 0:
                return False
            else:
                return all([candidate % prime != 0 for prime in primes])

        def get_next_prime(start_number, primes):
            curr_number = start_number
            while True:
                if is_prime(curr_number, primes):
                    return curr_number
                else:
                    curr_number += 2

        count = 2
        current_prime = 3
        primes = [2, 3]
        while count < number:
            current_prime = get_next_prime(current_prime + 2, primes)
            primes.append(current_prime)
            count += 1

        return primes

    def get_answer(self):
        return self.get_prime_number()


class Problem8(Problem):
    @staticmethod
    def calc_cum_prod(list_of_nums):

        cum_prod = 1
        for num in list_of_nums:
            if num == 0:
                return 0
            cum_prod *= num

        return cum_prod

    def get_largest_product(self, n=13):

        sequence = "".join([
            "73167176531330624919225119674426574742355349194934",
            "96983520312774506326239578318016984801869478851843",
            "85861560789112949495459501737958331952853208805511",
            "12540698747158523863050715693290963295227443043557",
            "66896648950445244523161731856403098711121722383113",
            "62229893423380308135336276614282806444486645238749",
            "30358907296290491560440772390713810515859307960866",
            "70172427121883998797908792274921901699720888093776",
            "65727333001053367881220235421809751254540594752243",
            "52584907711670556013604839586446706324415722155397",
            "53697817977846174064955149290862569321978468622482",
            "83972241375657056057490261407972968652414535100474",
            "82166370484403199890008895243450658541227588666881",
            "16427171479924442928230863465674813919123162824586",
            "17866458359124566529476545682848912883142607690042",
            "24219022671055626321111109370544217506941658960408",
            "07198403850962455444362981230987879927244284909188",
            "84580156166097919133875499200524063689912560717606",
            "05886116467109405077541002256983155200055935729725",
            "71636269561882670428252483600823257530420752963450"
        ])
        sequence = [int(c) for c in sequence]

        max = 0
        for idx in xrange(n - 1, len(sequence)):
            sub_seq = sequence[idx + 1 - n: idx + 1]
            cum_prod = Problem8.calc_cum_prod(sub_seq)
            if cum_prod > max:
                max = cum_prod

        return max

    def get_answer(self):
        return self.get_largest_product()


class Problem9(Problem):
    def get_answer(self):
        for a in xrange(1, 999):
            for b in xrange(a, 999):
                lhs = a ** 2 + b ** 2
                rhs = (1000 - a - b) ** 2
                if lhs == rhs:
                    return a, b

def problem10():
   primes = sieves.Erasosthenes.primes_less_than(2000000)
   print sum(primes)



def problem11():
    s = """
        08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
        49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
        81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
        52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
        22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
        24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
        32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
        67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
        24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
        21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
        78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
        16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
        86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
        19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
        04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
        88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
        04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
        20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
        20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
        01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 
    """

    rows = []
    for line in s.strip().split('\n'):
        rows.append([int(n) for n in line.split()])

    matrix = np.array(rows)
    row_max = np.max([product.largest_product_in_list(matrix[idx, :], 4)[0] for idx in xrange(len(matrix))])
    col_max = np.max([product.largest_product_in_list(matrix[:, idx], 4)[0] for idx in xrange(len(matrix))])

    diags = []
    horizontal_flip_matrix = np.fliplr(matrix)
    for idx in xrange(20):
        above = np.diag(matrix, idx)
        below = np.diag(matrix, -idx)
        above_flip = np.diag(horizontal_flip_matrix, idx)
        below_flip = np.diag(horizontal_flip_matrix, -idx)
        if len(above) >= 4:
            diags.append(product.largest_product_in_list(above)[0])
            diags.append(product.largest_product_in_list(below)[0])
            diags.append(product.largest_product_in_list(above_flip)[0])
            diags.append(product.largest_product_in_list(below_flip)[0])

    diag_max = np.max(diags)

    print np.max([diag_max, row_max, col_max])


def problem12():

    curr_i = 1
    total = 0
    max_factors = 0
    while True:
        total += curr_i
        n_factors = len(factors.factors_of_n(total))
        curr_i += 1
        if n_factors > max_factors:
            max_factors = n_factors
        print total, n_factors, max_factors
        if n_factors > 500:
            break




if __name__ == "__main__":
    problem12()
