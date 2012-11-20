'''
The 5-digit number, 16807=7**5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''

from math import log10

def main():
    '''
    10**1は 2ケタなので, 探索する底は 2<=a<=9でよい.
    a**nがnケタならば, n - 1 < n * log10(a) < nより, 
    n * (1 - log10(a)) < 1 である.
    '''
    ans = set()
    
    for a in range(2, 10):
        n = 1
        while n * (1 - log10(a)) < 1:
            if len(str(a**n)) == n:
                ans.add(a**n)
            n += 1
    
    return len(ans) + 1 #1**1の分を忘れずに
    
if __name__ == '__main__':
    print(main())
    