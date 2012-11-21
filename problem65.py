'https://projecteuler.net/problem=65'

from fractions import Fraction
from intlib import digit_sum

def main():
    loop = 99
    if loop % 3 == 2:
        a = Fraction(2*(1 + loop//3), 1)
    else:
        a = Fraction(1, 1)
    for i in range(loop - 1, 0, -1):
        if i % 3 == 2:
            a = 2*(1 + i//3)  + 1 / a
        else:
            a = 1 + 1 / a
    return digit_sum((2 + 1 / a).numerator)

if __name__ == '__main__':
    print(main())