'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series,
1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

if __name__ == '__main__':
    s = 0
    for i in range(1, 1001):
        a = 1
        for j in range(i):
            a = (a * i) % 10 ** 10
        s = (s + a) % 10 ** 10
    print(s)