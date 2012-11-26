'''
Determine the number of factorial chains that
contain exactly sixty non-repeating terms.
'''

import math

fact_list = [math.factorial(n) for n in range(10)]

def factorial(n):
    return fact_list[n]

def memoize(func):
    memo = {}
    def _func(*args):
        if args not in memo: memo[args] = func(*args)
        return memo[args]
    return _func

@memoize
def next_num(n):
    ans = 0
    while n:
        ans += factorial(n % 10)
        n = n // 10
    return ans

def dfs(n):
    visited = []
    while n not in visited:
        visited.append(n)
        n = next_num(n)
    return len(visited)

def main():
    return sum((1 for n in range(1000000) if dfs(n) == 60))

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))