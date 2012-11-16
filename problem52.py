'''
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

import itertools

def main():
    for x in itertools.count(1):
        digits = sorted(str(x))
        flag = True
        for k in range(2, 7):
            flag = flag and digits == sorted(str(k*x))
        if flag: return x

if __name__ == '__main__':
    print(main())