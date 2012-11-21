'https://projecteuler.net/problem=64'

from intlib import gcd, is_square
from math import floor

def cycle(n):
    '''
    √nの連分数展開のサイクルを求める.
    (a√n + b)/c を tuple (a, b, c) で表す.
    ただし, a, b, cに共通の因数はないものとする.
    '''
    ls = []
    m = floor(n**0.5)
    a, b, c = 1, -m, 1
    while (a, b, c) not in ls:
        ls.append((a, b, c))
        m = floor(c/(a*n**0.5 + b))
        a, b, c = a*c, -b*c - m*(n*a**2 - b**2), n*a**2 - b**2
        d = gcd(gcd(a, b), c)
        a, b, c = a//d, b//d, c//d
    return len(ls) - 1

def main():
    return sum((1 for n in range(2, 10001)
                if not is_square(n) and cycle(n) % 2))
    
if __name__ == '__main__':
    print(main())
