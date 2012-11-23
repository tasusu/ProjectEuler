'''
The cube, 41063625 (345**3), can be permuted to produce two other cubes:
56623104 (384**3) and 66430125 (405**3). In fact, 41063625 is the smallest
cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

import itertools
from collections import defaultdict

def main():
    length = 5
    digit = 1
    d = defaultdict(list)    
    for i in itertools.count(1):
        if i**3 > 10**digit:
            # 解があるかどうかチェック
            tmp = [val[0] for key, val in d.items() if len(val) == length]
            if tmp: return min(tmp)
            # 解がない場合はリセット
            d = defaultdict(list)
            digit += 1
            
        key = ''.join(sorted(str(i**3)))
        d[key].append(i**3)
        
        
if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))