'''
Exploring the shortest path from one corner of a cuboid to another.
'''

# GLOBALS
squares = [i * i for i in range(1, int(1000000 * 5 ** 0.5))]
squares_set = set(squares)


def num_of_sols(M):
    '''
    1辺がMまでの部屋のパスで整数長の個数を返す.
    a*b*c(c<=b<=a<=M)の部屋を考える.
    このときの最短パス長の2乗は a**2 + (b+c)**2 <= 5*a**2 である.
    平方数sに対し, s-a**2が再び平方数になっていれば,
    sを最短パス長にもつような, bとcが存在する.
    l = (s - a**2) ** 0.5 とすると, b + c = l かつ 1<=c<=b<=a となる
    b,c の個数は l <= a のとき l//2, l > a のとき, l//2 - (l - a - 1)
    '''
    ans = 0

    for a in range(1, M + 1):
        for s in squares:
            if s > 5 * a * a:
                break
            if s - a ** 2 in squares_set:
                l = int((s - a ** 2) ** 0.5)
                ans += l // 2 - max((l - a - 1, 0))

    return ans


def main():
    '''
    binary searchによってMを出す.
    アルゴリズムの実行中, num_of_sol(lo) <= 1000000 < num_of_sol(hi)
    であることが保証されるので, loとhiの差が1になった時点で終了する.
    '''
    lo = 100
    hi = 100
    while num_of_sols(hi) <= 1000000:
        hi *= 2

    while True:
        mid = (lo + hi) // 2
        l = num_of_sols(mid)
        if l > 1000000:
            hi = mid
        else:
            lo = mid

        if hi - lo == 1:
            return hi


if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
