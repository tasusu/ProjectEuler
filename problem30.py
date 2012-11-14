'''
Surprisingly there are only three numbers that can be written as
the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of
fifth powers of their digits.
'''

def sum_of_digits(n, pow = 1):
    s = 0
    while n > 0:
        d = n % 10
        s += d ** pow
        n = n // 10
    return s    

if __name__ == '__main__':
    '9**5 * x - 10**(x-1) = 0を解くと, x < 7.'
    
    ans = sum([n for n in range(2, 10**7)
               if n == sum_of_digits(n, pow=5)])
    
    print(ans)
    