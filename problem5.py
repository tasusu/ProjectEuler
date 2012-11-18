# -*- coding: utf-8 -*-

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def div_20():
    i = 1
    while True:
        k = i * 9699690
        if not any([k  % j for j in range(1,21)]):
            return k
        i = i + 1
        
def gcd(a,b): return b and gcd(b, a % b) or a
def lcm(a,b): return a * b / gcd(a,b)


if __name__ == '__main__':
    n = 1
    for i in range(1, 21):
        n = lcm(n, i)
    print(n)