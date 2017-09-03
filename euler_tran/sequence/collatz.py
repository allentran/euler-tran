


class CollatzCache(object):
    def __init__(self):
        super(CollatzCache, self).__init__()
        self.cache = {}

    def get_cache_count(self, n, count=0):
        if n in self.cache:
            return self.cache[n] + count

    @staticmethod
    def next_collatz(n):
        if n % 2 == 0:
            return n / 2
        return 3 * n + 1

    def until_n0(self, n, count=0):
        if n == 1:
            return count + 1
        next_n = self.next_collatz(n)
        cache_count = self.get_cache_count(next_n, count + 1)
        if cache_count:
            return cache_count
        steps = self.until_n0(next_n, count + 1)
        self.cache[next_n] = steps - count - 1
        return steps
