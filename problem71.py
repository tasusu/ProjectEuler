'''
https://projecteuler.net/problem=71
'''

from fractions import Fraction
import math

def main():
    '''
    3/7 より小さい分数で, 最大のものを保持する.
    各分母dに対し, n/d < 3/7 < (n+1)/d
    <=> (3d-7)/7 < n < 3d/7.
    '''
    ans = Fraction(0, 1)
    dist = 1
    
    for d in range(10**6//2, 10**6 + 1):
        lo = math.ceil((3*d-7)/7)
        hi = math.floor(3*d/7)
        for n in range(lo, hi+1):
            if 0 < 3/7 - n/d < dist:
                dist = 3/7 - n/d
                ans = Fraction(n, d)
            
    return ans.numerator

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))