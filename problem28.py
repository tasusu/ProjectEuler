'''
Problem 28
https://projecteuler.net/problem=28
'''

if __name__ == '__main__':
    s = 1
    n = 1
    for i in range(1, 1001//2 + 1):
        for j in range(4):
            n = n + 2 * i
            s += n
    print(s)