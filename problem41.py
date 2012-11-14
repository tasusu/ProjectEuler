'''
We shall say that an n-digit number is pandigital if it makes
use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

import itertools
import intlib

if __name__ == '__main__':
    '''
    4<= n <=9 を探索すれば良い.
    1+2+3+4+5 = 15 より, 5ケタのpandigital numberは3の倍数
    となるから, 調べなくて良い.
    1+2+3+4+5+6 = 21
   1 + ... + 8 = 36
   1 + ... + 9 = 45  
    より6, 8, 9ケタも同様に対象外.
    7ケタのうち, 末尾が3,7の数を調べれば良い.
    '''
    
    max_prime = 2143
    for n in itertools.permutations('1234'):
        n = int(''.join(n))
        if intlib.is_prime(n):
            max_prime = max((n, max_prime))
    
    for n in itertools.permutations('124567'):
        n = int(''.join(n) + '3')
        if intlib.is_prime(n):
            max_prime = max((n, max_prime))
            
    for n in itertools.permutations('123456'):
        n = int(''.join(n) + '7')
        if intlib.is_prime(n):
            max_prime = max((n, max_prime))
    
    print(max_prime)
        