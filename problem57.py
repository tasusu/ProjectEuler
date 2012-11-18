'''
It is possible to show that the square root of two can be
expressed as an infinite continued fraction.

√2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408,
but the eighth expansion, 1393/985, is the first example where
the number of digits in the numerator exceeds the number of digits
in the denominator.

In the first one-thousand expansions, how many fractions contain
a numerator with more digits than denominator?
'''

from fractions import Fraction

def cont_frac(n):
    denom = Fraction(2,1)
    i = 0
    while i < n:
        yield 1 + 1/denom
        denom = 2 + 1/denom
        i += 1
        
def check(frac):
    return len(str(frac.numerator)) > len(str(frac.denominator))
    
if __name__ == '__main__':
    print(len([1 for frac in cont_frac(1000) if check(frac)]))
        
        