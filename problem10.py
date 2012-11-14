'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

import math
import time

def furui(n):
    primes = [2]
    ls = [i for i in range(3, n + 1 ,2)]
    while ls:
        p = ls[0]
        if p > math.sqrt(n):
            primes += ls
            break
        primes.append(p)
        ls = [i for i in ls if i % p]
    return primes

def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False

def sieve(n):
    s = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if s[x]: mark(s, x)
    return [i for i in range(0,n) if s[i] and i > 1]
    
if __name__ == '__main__':
    t1 = time.clock()
    a = sum(furui(2000000))
    t2 = time.clock()
    print (a, t2 - t1, 'sec')
    t1 = time.clock()
    a = sum(sieve(2000000))
    t2 = time.clock()
    print (a, t2 - t1, 'sec')
    
    