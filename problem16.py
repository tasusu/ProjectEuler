'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

import math
import time


def digits(n):
    s = 0
    while n > 0:
        s = s + (n % 10)
        n = n // 10
    return s

if __name__ == '__main__':
    t1 = time.clock()
    d = [int(n) for n in str(2**1000)]
    t2 = time.clock()
    print(sum(d), t2 - t1)
    t1 = time.clock()
    n = digits(2**1000)
    t2 = time.clock()
    print(n, t2 - t1)
    