'''
https://projecteuler.net/problem=58
'''

import intlib
def diags():
    i = 1
    k = 1
    while True:
        d = 2*i
        yield [k+d, k+2*d, k+3*d, k+4*d]
        k = k+4*d
        i+= 1

def main():
    p = 0
    for i, d in enumerate(diags()):
        p += len([n for n in d if intlib.is_prime(n)])
        r = p/(5+4*i)
        if r < 0.1: return 2*i + 3

if __name__ == '__main__':
    print(main())