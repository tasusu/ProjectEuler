'''
How many fractions lie between 1/3 and 1/2 in a
sorted set of reduced proper fractions?
'''

from fractions import Fraction, gcd
import math

def main():
    '''3/7 より小さい分数で, 最大のものを保持する.
    (n-1)/d <= 1/3 < n/d <=> d/3 <= n < (d-3)/3,
    n/d <= 1/2 < (n+1)/d <=> (d-2)/2 < n <= d/2.'''
    
    ans = 0
    for d in range(2, 12001):
        lo = math.ceil(d/3)
        hi = math.floor(d/2)
        ans += sum((1 for n in range(lo, hi+1)
                     if 1/3 < n/d < 1/2 and gcd(n, d) == 1))    
    return ans

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))