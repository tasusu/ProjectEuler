'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle         Tn=n(n+1)/2         1, 3, 6, 10, 15, ...
Pentagonal         Pn=n(3n-1)/2         1, 5, 12, 22, 35, ...
Hexagonal         Hn=n(2n-1)         1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

import itertools

def main():
    tri_iter = (n*(n+1)//2 for n in itertools.count(1))
    pent_iter = (n*(3*n-1)//2 for n in itertools.count(1))
    hex_iter = (n*(2*n-1) for n in itertools.count(1))
    
    pent_set = set()
    hex_set = set()
    ans = []
    
    for n in tri_iter:
        pent_set.add(next(pent_iter))
        hex_set.add(next(hex_iter))
        if n in pent_set and n in hex_set: ans.append(n)
        if len(ans) > 2 : return ans[-1]
    

if __name__ == '__main__':
    import time
    t0 = time.clock()
    print(main())
    t1 = time.clock()
    print(t1-t0)
