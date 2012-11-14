# -*- coding: utf-8 -*-

'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:
1£1 + 150p + 220p + 15p + 12p + 31p

How many different ways can £2 be made using any number of coins?
'''

import math
import time

def count(tpl, n):
    if len(tpl) == 1 or n == 0:
        return 1
    m = n // tpl[0] + 1
    s = 0
    for i in range(m):
        s += count(tpl[1:], n - i * tpl[0])
    return s

def memo_count(tpl, n):
    if len(tpl) == 1 or n == 0:
        return 1
    if not (tpl, n) in cache:
        m = n // tpl[0] + 1
        s = 0
        for i in range(m):
            s += memo_count(tpl[1:], n - i * tpl[0])
        cache[(tpl, n)] = s
    return cache[(tpl, n)]
        
if __name__ == '__main__':
    cache = {}
    t1 = time.clock()
    print(count((100, 50, 20, 10, 5, 2, 1), 200) + 1)
    t2 = time.clock()
    print('Normal:', t2 - t1)
    t1 = time.clock()
    print(memo_count((100, 50, 20, 10, 5, 2, 1), 200) + 1)
    t2 = time.clock()
    print('Memo:', t2 - t1)
    
    
    