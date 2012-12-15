'''
Investigating numbers that can be expressed as the sum of a prime square, cube,
and fourth power?
'''

import intlib


def main():
    TARGET = 50000000
    primes = intlib.primes(int(TARGET ** 0.5))
    p_squares = [p ** 2 for p in primes if p ** 2 <= TARGET]
    p_cubes = [p ** 3 for p in primes if p ** 3 <= TARGET]
    p_fths = [p ** 4 for p in primes if p ** 4 <= TARGET]
    ans = set()
    for a in p_squares:
        for b in p_cubes:
            for c in p_fths:
                if a + b + c <= TARGET:
                    ans.add(a + b + c)

    return len(ans)


if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
