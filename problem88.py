'''
Exploring minimal product-sum numbers for sets of different sizes.
'''


def prod(iterable):
    ans = 1
    for a in iterable:
        ans *= a
    return ans


def gen_product_sum(lo, hi, k):
    '''
    lo <= a1 * ... * ak <= hi となる[a1, ..., ak]を順番に返す.
    '''
    if k == 1:
        for d in range(lo, hi + 1):
            yield [d]

    for d in range(lo, hi + 1):
        for seq in gen_product_sum(d, hi // d, k - 1):
            yield [d] + seq


def main():
    ans = {}
    for prod_len in range(2, 16):
        for a in gen_product_sum(2, 24000, prod_len):
            n = prod(a)
            k = len(a) + n - sum(a)
            if n < ans.get(k, float('inf')) and k <= 12000:
                ans[k] = n

    return sum({v for v in ans.values()})

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
