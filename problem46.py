'''
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2*1**2
15 = 7 + 2*2**2
21 = 3 + 2*3**2
25 = 7 + 2*3**2
27 = 19 + 2*2**2
33 = 31 + 2*1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of
a prime and twice a square?
'''

import itertools
import intlib

def main():
    _max = 10**4
    odd_iter = (2*n + 1 for n in itertools.count(1))
    primes = intlib.primes(_max)
    primes_set = set(primes) #membership判定用set
    
    for n in odd_iter:
        if n > _max: return 'Not found.'
        if n in primes_set: continue
        flag = True
        for p in primes:
            if p > n: break
            if intlib.is_square((n - p)//2):
                flag = False
                break
        if flag:
            return n

if __name__ == '__main__':
    print(main())
            