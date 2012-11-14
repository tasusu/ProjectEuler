'''
https://projecteuler.net/problem=40
'''

if __name__ == '__main__':
    s = ''.join([str(i) for i in range(10**6)])
    print(s[12])
    ans = 1
    for i in range(7):
        ans *= int(s[10**i])
    print(ans)