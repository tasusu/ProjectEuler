'''
Problem 39
----------------------
If p is the perimeter of a right angle triangle with
integral length sides, {a,b,c}, there are exactly
three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

def count_sols(p):
    ans = 0
    for a in range(1, p//3):
        for b in range(a + 1, (p - a)//2):
            c = p - a - b
            if a**2 + b**2 == c**2 :
                ans += 1
    return ans

def main():
    ans = 0
    n = 0
    for p in range(1, 1001):
        m = count_sols(p)
        if n < m:
            ans = p
            n = m
    return ans
    

if __name__ == '__main__':
    print(__doc__)
    print(count_sols(120))
    print(main())