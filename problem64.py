'https://projecteuler.net/problem=64'

from intlib import is_square
from math import floor

def cycle(n):
    before = []
    a, m, d = floor(n**0.5), 0, 1 #a は常に (√n + m)//d の整数部分
    ans = [a]
    while (a, m, d) not in before:
        before.append((a, m, d))
        m = d * a - m
        d = (n - m**2)//d
        a = floor((ans[0] + m)//d)
        ans.append(a)
        
    return len(ans[:-1])

def main():
    return sum((1 for n in range(2, 10001)
                if not is_square(n) and cycle(n) % 2))
    
if __name__ == '__main__':
    print(main())
