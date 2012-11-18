'''
https://projecteuler.net/problem=55
'''

def is_palindromic(n):
    return str(n) == str(n)[::-1]

def is_Lychrel(n):
    for i in range(50):
        n = n + int(str(n)[::-1])
        if is_palindromic(n): return False
    return True

if __name__ == '__main__':
    #test
    #print(is_palindromic(121))
    #print(is_Lychrel(349))
    print(len([1 for n in range(10000) if is_Lychrel(n)]))