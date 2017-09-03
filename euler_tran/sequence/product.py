import numpy as np


def largest_product_in_list(l, n=4):
    assert len(l) >= n

    if n == 1:
        return np.max(l), np.argmax(l)

    max_seq = l[:n]
    curr_max = np.product(l[:n])
    for idx in xrange(n, len(l) + 1):
        new_max = np.product(l[idx - n:idx])
        if new_max > curr_max:
            max_seq = l[idx - n: idx]
            curr_max = new_max
    return curr_max, max_seq

