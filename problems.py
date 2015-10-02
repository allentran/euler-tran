
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
        for num_i in xrange(self.min, self.max+1):
            for num_j in xrange(self.min, self.max+1):
                product = num_i * num_j
                if product >= curr_max and self.ispalindrome(num_i*num_j):
                    curr_max = product
        return curr_max

    def get_answer(self):
        print self.max_palin()

# problem 5

class Problem5(Problem):

    def __init__(self):

        self.primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def findPrimeFactors(self, num):
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

    def findSmallestProd(self, max_prod):

        prods = range(1, max_prod+1)
        primes = {}
        for num in prods:
            factors = self.findPrimeFactors(num)
            for f in factors:
                if f in primes:
                    if factors[f] > primes[f]:
                        primes[f] = factors[f]
                else:
                    primes[f] = factors[f]
        cum_prod = 1
        for f in primes:
            cum_prod *= f**primes[f]
                
        return primes, cum_prod

    def get_answer(self):
        print self.findSmallestProd(20)

class Problem6(Problem):

    def findSum(self, num):

        cum_squares = 0
        cum_sum = 0
        for ii in xrange(1, num+1):
            cum_squares += ii**2
            cum_sum += ii
        return cum_sum**2 - cum_squares

    def get_answer(self):
        print self.findSum(100)

class Problem7(Problem):

    def get_prime_number(self, number = 10001):

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

        max=0
        for idx in xrange(n - 1, len(sequence)):
            sub_seq = sequence[idx + 1 - n: idx + 1]
            cum_prod = Problem8.calc_cum_prod(sub_seq)
            if cum_prod > max:
                max = cum_prod

        return max

    def get_answer(self):
        return self.get_largest_product()

if __name__ == "__main__":
    problem = Problem8()
    print problem.get_answer()