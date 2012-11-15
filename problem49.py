'''
The arithmetic sequence, 1487, 4817, 8147, in which each of
the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or
3-digit primes, exhibiting this property, but there is one other
4-digit increasing sequence.

What 12-digit number do you form by concatenating the three
terms in this sequence?
'''

import intlib
import itertools

if __name__ == '__main__':
    four_digit_primes = [p for p in intlib.primes(10000) if 1000 < p < 10000]
    for a, b, c in itertools.combinations(four_digit_primes, 3):
        if (c-b == b-a and sorted(str(a)) == sorted(str(b)) == sorted(str(c))):
            print(a, b, c)