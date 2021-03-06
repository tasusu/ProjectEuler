'''
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2.
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum
and difference is pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
'''

import math
import itertools

def is_square(x):
    return math.floor(math.sqrt(x))**2 == x

def is_pentagonal(x):
    return is_square(24*x + 1) and math.floor(math.sqrt(24*x + 1)) % 6 == 5

def pentagonal(n):
    return n * (3*n - 1) // 2

def stupid_main():
    D = float("inf")
    i = 1
    j = 2
    Pi = pentagonal(i)
    Pj = pentagonal(j)
    while 3*i + 1 < D:
        j = i + 1
        Pj = pentagonal(j)
        while j <= (Pi - 1) // 3 and Pj - Pi < D:
            if is_pentagonal(Pj - Pi) and is_pentagonal(Pj + Pi):
                D = min((D, Pj - Pi))
                print('found {}, {}, {}'.format(Pi,Pj,D))
            j += 1
            Pj = pentagonal(j)
        
        i += 1
        Pi = pentagonal(i)
        print(i,j,D)
        
    return D


def main_guess():
    penta_iter = (n*(3*n-1)//2 for n in itertools.count(1))
    penta_set = set()
    D = float('inf')
    
    'x:=Pi+Pjとし, xを順に大きくして探索する.'
    for x in penta_iter:
        penta_set.add(x)
        for y in (y for y in penta_set if y < D):
            'y:=Pj-Piとし, yも順に大きくする.'
            if (x+y)/2 in penta_set and (x-y)/2 in penta_set:
                return y
            
def main():
    penta_iter = (n*(3*n-1)//2 for n in itertools.count(1))
    penta_set = set()
    D = float('inf')
    
    for j, Pj in enumerate(penta_iter):
        if 3*j - 2 >= D: break #Pj - Pj-1 >= D よりこれ以上の探索は不要.
        penta_set.add(Pj)
        for Pi in (Pi for Pi in penta_set if Pj - Pi < D):
            if is_pentagonal(Pi + Pj) and Pj-Pi in penta_set:
                D = min((D, Pj-Pi))
    return D

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    print(time.time() - t1)
            