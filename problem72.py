'''
https://projecteuler.net/problem=72
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
    factors_dict = make_dict(1000001)
    return sum(phi(d, factors_dict[d]) for d in range(2, 1000001))

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))