'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician
in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
'''

import fractions

def common_digits(a, b):
    a = {d for d in str(a)}
    b = {d for d in str(b)}
    return a & b

def delete_digit(a, d):
    a = str(a)
    if a == d + d: return int(d)
    else: return int(str(a).strip(d))

def nontrivial(a, b):
    '''
    a/b = e/f <=> af=be
    '''
    for d in common_digits(a, b):
        if d == '0': continue
        e = delete_digit(a, d)
        f = delete_digit(b, d)
        if a * f == b * e : return True
    
    return False

def main():
    prod = fractions.Fraction(1, 1)
    
    for a in range(10, 100):
        for b in range(a + 1, 100):
            if nontrivial(a, b):
                print(fractions.Fraction(a, b), '{}/{}'.format(a, b))
                prod *= fractions.Fraction(a, b)
                
    print(prod.denominator)

if __name__ == '__main__':
    main()