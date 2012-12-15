'''
Exploring minimal product-sum numbers for sets of different sizes.
'''

import itertools


def product_sum(n, k):
    '''
    nがk個のproduct_sumで書けるか
    '''
    return _product_sum(n, n, k)


def _product_sum(n, target, k):
    '''
    targetがnのk個への因子分解の因子和で書けるか
    '''
    if target < 0:
        return False

    if n == 1:
        return target == k

    for d in range(2, n + 1):
        if n % d == 0 and _product_sum(n // d, target - d, k - 1):
            return True

    return False


def main():
    ans = set()
    for k in range(2, 12001):
        for n in itertools.count(k):
            if product_sum(n, k):
                ans.add(n)
                break
    return sum(ans), len(ans)

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
