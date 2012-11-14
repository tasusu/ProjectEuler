'''
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254,
containing multiplicand, multiplier, and product is
1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
'''


def is_pantagonal(a, b):
    s = str(a) + str(b) + str(a * b)
    if len(s) != 9: return False
    
    table = [False for i in range(9)]
    for a in s:
        n = int(a)
        if n == 0: return False
        elif table[n - 1] == True: return False
        else: table[n - 1] = True
    
    return True

def main():
    '''
    xケタ  * yケタ の数は x + y - 2 ケタ ~ x + yケタ.
        合計の桁数は 2(x+y) -2 ~ 2(x+y) ケタ.
    x = 1 => y = 4, 5
    x = 2 => y = 3, 4
    x = 3 => y = 3
    '''
    
    digits = [(1,4), (1,5), (2,3), (2,4), (3,3)]
    prods = set()
    
    for x, y in digits:
        for a in range(10**(x-1) + 1, 10**x):
            for b in range(10**(y-1) + 1, 10**y):
                if a < b and is_pantagonal(a, b) and a*b not in prods:
                    prods.add(a * b)
    
    return sum(prods)

if __name__ == '__main__':
    print(main())
    
    