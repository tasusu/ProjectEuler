'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math
import time

def divisors(n):
    divs = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divs.append(i)
            if n/i not in divs:
                divs.append(n/i)
    divs.sort()
    return divs
   
def sum_of_two(n, abd):
    for i in abd:
        if i > n / 2:
            break
        if cache[n - i]:
            return True
    return False



if __name__ == '__main__':
    cache = [False] * 28124
    t1 = time.clock()
    for i in range(1, 28124):
        if sum(divisors(i)) > i:
            cache[i] = True
    abd = [i for i in range(28124) if cache[i]]
    print(sum([i for i in range(1, 28124) if not sum_of_two(i, abd)]))
    t2 = time.clock()
    print('Runtime: {} s'.format(t2 - t1))
        