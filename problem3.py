# -*- coding: utf-8 -*-

'''The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?'''

import math

def primes():
    i = 2
    tmp = []
    while True:
        flag = True
        for p in tmp:
            if not i % p:
                flag = False
                break
        if flag:
            yield i
            tmp.append(i)
        i = i + 1

if __name__ == '__main__':
    n = 600851475143
    i = 1
    while n > 1:
        i = i + 1
        while n % i == 0:
            n = n/i
    print(i)
    