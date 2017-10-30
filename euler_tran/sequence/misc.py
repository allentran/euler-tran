import numpy as np


def fibonacci_generator():
    prev = [0, 1]
    idx = 1
    while True:
        yield idx, prev[1]
        idx += 1
        prev = [prev[1], prev[0] + prev[1]]


def recurring_fraction(denom):
    n = 1 % denom
    seen = set()
    count = 0
    while True:
        n = 10 * n % denom
        if n not in seen:
            seen.add(n)
            count += 1
        else:
            return count


class TriangleNumber(object):
    def __init__(self, max_n):
        self.curr_idx = 1
        self.set = {1}
        self.curr_max = 1

        self.expand_upto(max_n)

    def expand_upto(self, max_element):
        if max_element > self.curr_max:
            j = self.curr_idx + 1
            while True:
                t_n = int(0.5 * j * (j + 1))
                self.set.add(t_n)
                self.curr_max = t_n
                if t_n > max_element:
                    self.curr_idx = j
                    break
                j += 1


class SquareDigitChain(object):
    def __init__(self):
        self.cache = {}
        self.str_cache = {}
        self.sq_cache = {n: n ** 2 for n in xrange(10)}

    def get_cache_end(self, n):
        if n in self.cache:
            return self.cache[n]

    def _next(self, n):
        squares = []
        str_n = str(n)
        for idx in xrange(len(str_n)):
            if str_n[idx:] in self.str_cache:
                squares.append(self.str_cache[str_n[idx:]])
                break
            else:
                c = int(str_n[idx])
                squares.append(self.sq_cache[c])
        return np.sum(squares)

    def get_end(self, n, seen):
        if n == 1:
            for prev_n in seen:
                self.cache[prev_n] = 1
            return 1
        elif n == 89:
            for prev_n in seen:
                self.cache[prev_n] = 89
            return 89
        else:
            next_n = self._next(n)
            self.str_cache[str(n)] = next_n
            cache_count = self.get_cache_end(next_n)
            if cache_count:
                for prev_n in seen:
                    self.cache[prev_n] = cache_count
                return cache_count
            return self.get_end(next_n, seen + [next_n])
