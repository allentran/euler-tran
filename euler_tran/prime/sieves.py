

class Erasosthenes(object):

    @staticmethod
    def primes_less_than(x):

        assert isinstance(x, int)
        primes = {2}
        integers = [False] * x
        curr_idx = 2
        while curr_idx < x:
            if not integers[curr_idx]:
                curr_prime = curr_idx
                curr_multiple = 1
                while curr_multiple * curr_prime < x:
                    integers[curr_multiple * curr_prime] = True
                    curr_multiple += 1
                primes.add(curr_prime)
            else:
                curr_idx += 1

        return primes

