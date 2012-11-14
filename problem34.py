'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

import math

factorials = [math.factorial(i) for i in range(10)]
diffs = [factorials[i+1] - factorials[i]  for i in range(9)]
# diffs[i] = (i+1)! - i!

def fac_sum_gen(n):
    s = 2
    for i in range(3, n):
        d = i % 10 #末尾を取得
        if d > 0: #末尾が0でないので桁上りがない場合
            s = s + diffs[d - 1]
        else: #桁上りがある場合:
            j = i
            s = 0
            while j > 0:
                s += factorials[j % 10]
                j = j // 10          
        
        yield (i, s)
    
def main():
    '''
    9! = 362880 より
    xケタの数の各ケタの階乗の和は 高々 362880x.
    これと 10 ** x を比較すると, x = 6.38 くらいで追いつけなくなる.
    '''
    return sum([n for n, s in fac_sum_gen(math.floor(10**6.38))
                if n == s])

if __name__ == '__main__':
    print(main())