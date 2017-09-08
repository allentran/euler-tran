import numpy as np

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
