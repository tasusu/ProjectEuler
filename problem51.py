'''
By replacing the 1st digit of *3, it turns out that six of
the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among
the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of
an eight prime value family.
'''

import intlib

def generate_from_wildcard(w):
    ans = set()
    for i in range(10):
        if w[0] == '*' and i == 0:
            continue #'*3'->'03'は含まない.
        ans.add(int(w.replace('*', str(i))))
    return ans

def wildcards(p):
    return (str(p).replace(a, '*') for a in {a for a in str(p)})

def main():
    primes = intlib.Primes(1000000)
    for p in primes:
        for w in wildcards(p):
            if [primes.is_prime(n) for n
                in generate_from_wildcard(w)].count(True) >= 8:
                return (p, w)
    
if __name__ == '__main__':
    print(main())