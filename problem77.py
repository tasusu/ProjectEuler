'''
What is the first value which can be written as the
sum of primes in over five thousand different ways?
'''

import intlib
import itertools

def pattern(n):
    pre_table = [0] * (n + 1)
    
    for x in range(0, n + 1, 2):
        pre_table[x] = 1
    
    primes = intlib.primes(n)
    
    for k in range(1, len(primes)):
        table = [0] * (n + 1)
        for i in range(n + 1):
            table[i] = sum(pre_table[i - j * primes[k]] for j in
                           range(0, i//primes[k] + 1))
            
        pre_table = table
        
    return pre_table[n]

def main():
    for n in itertools.count(10):
        if pattern(n) > 5000: return n

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))