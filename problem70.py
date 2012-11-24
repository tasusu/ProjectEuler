'''
Euler's Totient function, φ(n) [sometimes called the phi function],
is used to determine the number of positive numbers less than or equal
to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8,
are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number,
so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation
of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the
ratio n/φ(n) produces a minimum.
'''

from collections import defaultdict

def phi(n, factors):
    numer= 1
    denom = 1
    for p in factors:
        numer *= (p - 1)
        denom *= p
    return (numer*n)//denom

def make_dict(n):
    factors_dict = defaultdict(set)
    s = [True] * n
    for x in range(2, n):
        if s[x]:
            factors_dict[x].add(x)
            for i in range(x + x, len(s), x):
                s[i] = False
                factors_dict[i].add(x)
            
    return factors_dict

def main():
    factors_dict = make_dict(10**7)
    min_ratio = 87109/79180
    ans = 87109
        
    for n in range(2, 10**7):
        factors = factors_dict[n]
        p = phi(n, factors)
        r = n / p
        if sorted(str(p)) == sorted(str(n)) and r < min_ratio:
            ans = n
            min_ratio = r
    return ans
                

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))