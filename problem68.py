'''
https://projecteuler.net/problem=68
'''

import itertools


def is_proper_ring(outer, inner):
    '各部分の和が等しいかチェック'
    total = outer[4] + inner[4] + inner[0]
    for i in range(4):
        if total != outer[i] + inner[i] + inner[i + 1]:
            return False
    return True


def ring_string(outer, inner):
    'ringが表す文字列を返す'
    ans = ''
    outer_min = min(outer)
    start = outer.index(outer_min)
    for d in range(5):
        ans += (str(outer[(start + d) % 5]) + str(inner[(start + d) % 5])
                + str(inner[(start + d + 1) % 5]))
    return ans


def main():
    '''
    16桁の数を求めるので, 必ず10は外周のノードにある. そこで,ringを時計回りに見て
    外周が x, y, z, w, 10
    内周が a, b, c, d, e （ただし aはxに隣接, bはyに隣接, ..., eは10に隣接)
    であるとき, outer = [x,y,z,w,10], inner=[a,b,c,d,e] の組でringを表現する.
    '''
    s = set()
    nums = list(range(1, 10))
    for outer in itertools.permutations(nums, 4):
        outer = list(outer) + [10]
        inner_nums = (i for i in nums if i not in outer)
        for inner in itertools.permutations(inner_nums):
            if is_proper_ring(outer, inner):
                s.add(int(ring_string(outer, inner)))

    return max(s)

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
