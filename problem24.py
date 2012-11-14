'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def find_n(ls, n):
    if len(ls) == 1:
        return ls[0]
    else:
        tmp = fact(len(ls) - 1)
        for i in range(len(ls)):
            if tmp * (i + 1) >= n: break
        return ls.pop(i) + find_n(ls, n - tmp * i)

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

if __name__ == '__main__':
    ls = [str(i) for i in range(10)]
    print(find_n(ls, 1000000))
    