import functools32

@functools32.lru_cache()
def factors_of_n(n, proper=False):
    if proper:
        factors = {1}
    else:
        factors = {1, n}
    for potential_factor in xrange(int(n ** 0.5), 1, -1):
        if n % potential_factor == 0:
            other_factor = n / potential_factor
            factors.add(potential_factor)
            factors.add(other_factor)
            factors = factors.union(factors_of_n(potential_factor))
            factors = factors.union(factors_of_n(other_factor))

    return set(factors)