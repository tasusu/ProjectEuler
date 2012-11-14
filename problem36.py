'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
'''

def is_palindromic(n):
    s = str(n)[::-1]
    return n == int(s)

def is_palindromic_binary(n):
    s = '{0:b}'.format(n)[::-1]
    return n == int(s, base = 2)

def main():
    ls = [n for n in range(1, 1000000)
           if is_palindromic(n) and is_palindromic_binary(n)]
    return sum(ls)
    
if __name__ == '__main__':
    print(main())