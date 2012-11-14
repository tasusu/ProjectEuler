'''
Problem 38
-------------
Take the number 192 and multiply it by each of 1, 2, and 3:
192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576.
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 
1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be 
formed as the concatenated product of an integer with (1,2, ... , n) 
where n > 1?
-------------
'''

def is_pantagonal(s):
    if len(s) != 9: return False
    s = set([a for a in s if a != '0'])
    return len(s) == 9

def is_concatenating(n):
    s = ''
    i = 1
    while len(s) < 9:
        s += str(i * n)
        i += 1
        
    if is_pantagonal(s):
        return int(s)
    return 0
        
def main():
    ans = 0
    for n in range(1, 10000):
        m = is_concatenating(n)
        ans = max((m, ans))
    return ans
    
if __name__ == '__main__':
    print(__doc__)
    print(main())