# problem 4

class Problem4:

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

# problem 5

class Problem5:

    def __init__(self, maxProd):

        self.maxProd = maxProd
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

    def findSmallestProd(self):

        prods = range(1,self.maxProd+1)
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

class Problem6:

    def findSum(self, num):

        cum_squares = 0
        cum_sum = 0
        for ii in xrange(1, num+1):
            cum_squares += ii**2
            cum_sum += ii
        return cum_sum**2 - cum_squares

