'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 * 7
15 = 3 * 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2 ** 2 *  7 * 23
645 = 3 * 5 * 43
646 = 2 * 17 * 19.

Find the first four consecutive integers to have four distinct primes factors.
What is the first of these numbers?
'''

import intlib

def main():
    max_ = 10**6
    primes = intlib.Primes(max_)
    
    i = 1
    while i + 4 < max_:
        flag = True
        for j in (3,2,1,0):
            if len(primes.prime_factors(i + j)) != 4:
                i = i + j + 1
                flag = False
                break
        if flag: return i
        
    return 'Not found'

if __name__ == '__main__':
    print(main())