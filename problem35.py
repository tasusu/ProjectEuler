'''
The number, 197, is called a circular prime because all rotations
of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from intlib import prime_set

primes = prime_set(10**6)

def is_cir_prime(n):
    s = str(n)
    for i in range(len(s)):
        if not int(s) in primes: return False
        s = s[1:] + s[0]
    
    return True

if __name__ == '__main__':
    cir_primes = [n for n in range(2, 10**6) if is_cir_prime(n)]
    print(cir_primes)
    print(len(cir_primes))