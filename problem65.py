'https://projecteuler.net/problem=65'

import itertools
from intlib import digit_sum, convergents

def cont_frac_of_e():
    'eの連分数表記 [2;1,2,1,1,4,1,1,6,1,..]の値を返すジェネレータ'
    yield 2
    for i in itertools.count(1):
        if i % 3 == 2: yield 2 * (i//3 + 1)
        else: yield 1

def main():
    for i, frac in enumerate(convergents(cont_frac_of_e())):
        if i == 99: break
    return digit_sum(frac.numerator)

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))