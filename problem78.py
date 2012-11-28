'''
Investigating the number of ways in which coins can be separated into piles.
'''

import intlib
import itertools
import numpy as np


def is_pentagonal(x):
    if intlib.is_square(1 + 24 * x) and int((1 + 24 * x) ** 0.5) % 6 == 5:
        return (int((1 + 24 * x) ** 0.5) + 1) // 6
    return 0


def is_pseudo_pentagonal(x):
    if intlib.is_square(1 + 24 * x) and int((1 + 24 * x) ** 0.5) % 6 == 1:
        return (int((1 + 24 * x) ** 0.5) - 1) // 6
    return 0


def coef(n):
    ans = 0
    if is_pentagonal(n):
        ans += (-1) ** is_pentagonal(n)
    if is_pseudo_pentagonal(n):
        ans += (-1) ** is_pseudo_pentagonal(n)
    return ans


def penta(n):
    return (3 * n * n - n) // 2


def partition_numbers():
    'Eulerの漸化式に基づく解法'
    p = [1]
    for n in itertools.count(1):
        v = 0
        for i in itertools.count(1):
            sgn = 1 if (i % 2) else -1
            if penta(i) > n:
                break
            v += sgn * p[n - penta(i)]
            if penta(-i) > n:
                break
            v += sgn * p[n - penta(-i)]

        yield v % 1000000
        p.append(v)


def faster_partition_numbers():
    'Numpyで高速化したバージョン'
    p = np.array([1], dtype=int)
    q = np.array([1], dtype=int)
    for n in itertools.count(1):
        p = np.append(p, 0)
        q = np.append(q, coef(n))
        p[-1] = -np.convolve(p, q, 'valid')[0] % 1000000
        yield p[-1]


def main():
    for i, p_n in enumerate(partition_numbers()):
        if p_n == 0:
            return i + 1


def faster():
    for i, p_n in enumerate(faster_partition_numbers()):
        if p_n == 0:
            return i + 1

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
    t1 = time.time()
    print(faster())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
