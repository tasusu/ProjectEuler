'https://projecteuler.net/problem=66'

from intlib import is_square, cont_frac_sqrt, convergents

def solve_pell(d):
    '''x**2-d*y**2=1 の最小解を求める.
    √dの第i次連分数近似を p_i/q_i とすると, (pi, pi)で方程式の解になるものが最小(らしい).'''
    for frac in convergents(cont_frac_sqrt(d)):
        p = frac.numerator
        q = frac.denominator
        if p**2 - d*q**2 == 1: return (p, q)

def main():
    ans = 0
    max_x = 0
    for d in range(1, 1001):
        if is_square(d): continue
        x, y = solve_pell(d)
        #print(d, (x, y))
        if x > max_x:
            ans = d
            max_x = x
    return ans

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))