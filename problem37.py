'''
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

 the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

from intlib import is_prime
import math

def is_left_truncatable(n):
    s = str(n)
    while s:
        if not is_prime(int(s)): return False
        s = s[1:]
    return True

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n): return False
        n = n // 10
    return True

def is_truncatable(n):
    return is_left_truncatable(n) and is_right_truncatable(n)

def right_truncs():
    ans = [2, 3, 5, 7]
    l = 0
    changed = True
    while changed:
        l += 1
        changed = False
        work_seq = [s for s in ans if math.floor(math.log10(s)) == l - 1]
        for s in work_seq:
            for x in (1, 3, 7, 9):
                n = 10 * s + x
                if is_prime(n):                    
                    ans.append(n)
                    changed = True
    
    return {s for s in ans if s > 10}

def force():
    ans = set()
    n = 11
    while len(ans) < 11:
        if is_truncatable(n):
            ans.add(n)
        n += 1
        
    return sum(ans)
    
def main():
    return sum([n for n in right_truncs() if is_left_truncatable(n)])
    
if __name__ == '__main__':
    print(main())
    print(force())