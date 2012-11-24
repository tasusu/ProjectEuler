'''
https://projecteuler.net/problem=69
'''

from collections import defaultdict
import intlib


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

def phi(n, factors):
    numer= 1
    denom = 1
    if not factors: return n - 1
    for p in factors:
        numer *= (p - 1)
        denom *= p
    return (numer*n)//denom

def main():
    '愚直に全探索する.'
    factors_dict = make_dict(1000000)
    
    n_max = 0
    ratio_max = 0
    for n in range(2, 1000001):
        factors = factors_dict[n]
        p = phi(n, factors)
        if n/p > ratio_max:
            n_max = n
            ratio_max = n/p
    return n_max

def clever():
    '''forumにあった回答.
    n/φ(n) = 1/((1-1/p1)...(1-1/pk)) より, 分母を大きくすれば良い.
    分母を大きくするには, nが小さい順にできるだけ多くの素因数を持てばよい.
    そのようなnは素数の積 2*3*5*... で1000000を超えないものである.'''
    ans = 1
    for p in intlib.prime_iter():
        if ans * p > 1000000: break
        ans *= p
    return ans

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))
    t1 = time.time()
    print(clever())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))