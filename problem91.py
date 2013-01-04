'''
Right triangles with integer coordinates
'''

import itertools

UPPER = 50


def is_right_triangle(p, q):
    '△OPQが直角三角形か調べる'
    x1, y1 = p
    x2, y2 = q

    if x1 * y2 - x2 * y1 >= 0:  # 時計回りにOPQの順になっていない場合と退化を除外
        return False

    return (x1 * x2 + y1 * y2 == 0  # ∠POQが直角
            or -x1 * (x2 - x1) - y1 * (y2 - y1) == 0  # ∠OPQが直角
            or -x2 * (x1 - x2) - y2 * (y1 - y2) == 0)  # ∠OQPが直角


def main():
    ans = 0
    for x1, y1 in itertools.product(range(UPPER + 1), repeat=2):
        for x2, y2 in itertools.product(range(UPPER + 1), repeat=2):
            p = (x1, y1)
            q = (x2, y2)
            if is_right_triangle(p, q):
                ans += 1
    return ans

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
