'''
Find the number of different lengths of wire
that can form a right angle triangle in only one way.
'''

from fractions import gcd
from collections import Counter

def gen_pythagolas(n):
    'a+b+c<=nを満たす原始ピタゴラス数の列挙'
    for m in range(2, int((n/2) ** 0.5) + 1):
        for n in range(1, m):
            if gcd(m, n) == 1 and (m + n) % 2 == 1:
                a = 2 * m * n
                b = m * m - n * n
                c = m * m + n * n
                if a > b: a, b = b, a
                yield (a, b, c)

def main():
    MAX = 1500000
    counter = Counter()
    for a, b, c in gen_pythagolas(MAX):
        s = a + b + c
        for x in range(s, MAX + 1, s):
            counter[x] += 1
               
    return sum((1 for k in counter.values() if k == 1))

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))