import math
import itertools
import random
import fractions

'''
 素数関係ない関数
------------------------
'''


def is_pandigit(s):
    '文字列sがpandigitかどうか調べる.'
    if len(s) != 9:
        return False
    s = set([a for a in s if a != '0'])
    return len(s) == 9


def is_square(x):
    'xが平方数か調べる.'
    if x < 0:
        return False
    return math.floor(math.sqrt(x)) ** 2 == x


def is_nth_power(x, n):
    'xがn乗数か調べる.'
    if x < 0:
        return False
    return (math.floor(math.pow(x, 1 / n)) ** n == x
            or math.ceil(math.pow(x, 1 / n)) ** n == x)


def digit_sum(n):
    'nの各桁の和'
    ans = 0
    while n:
        ans += n % 10
        n = n // 10
    return ans

'''
連分数
--------------------------
'''


def cont_frac_sqrt(n):
    '√nの連分数[a0;a1,a2,..]を次々に返すジェネレータを返す.'
    if is_square(n):
        return [math.floor(n ** 0.5)]
    before = []
    a, m, d = math.floor(n ** 0.5), 0, 1  # a は常に (√n + m)//d の整数部分
    ans = [a]
    while (a, m, d) not in before:
        before.append((a, m, d))
        m = d * a - m
        d = (n - m ** 2) // d
        a = math.floor((ans[0] + m) // d)
        ans.append(a)

    return cont_frac_gen(ans[:-1])


def cont_frac_gen(cont_frac_ls):
    '有限リスト [a0;a1,a2,..] で表される連分数をジェネレータに変換.'
    yield cont_frac_ls[0]
    for a in itertools.cycle(cont_frac_ls[1:]):
        yield a


def convergents(cont_frac):
    'cont_fracで表現される連分数のconvergentを返すジェネレータ. 返り値はfraction.'
    a0 = next(cont_frac)
    h1, h2, k1, k2 = a0, 1, 1, 0
    for ai in cont_frac:
        yield fractions.Fraction(h1, k1)
        h1, h2 = ai * h1 + h2, h1
        k1, k2 = ai * k1 + k2, k1

'''
素数を扱う関数.
これらの関数はO(1)回しか呼ばない, あるいは非有界な範囲の整数に対し実行するときに有効.
有界な範囲で何回も呼ぶ場合は, 後述のPrimesクラスの方が速い.
--------------------------
'''


def is_prime(n):
    'nが素数かどうか判定する. 定数回しか呼ばないときに有効.'
    if n <= 1:
        return False
    for i in range(2, int(math.floor(n ** 0.5)) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_rand(n, repeat=5):
    'Miller-Rabin素数判定法. repeatは繰り返し回数.'
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d & 1 == 0:
        s += 1
        d = d >> 1
    for i in range(repeat):
        a = random.randint(1, n - 1)
        y = pow(a, d, n)
        if y != 1:
            j = 0
            while y != n - 1 and j < s:
                y = y * y % n
                j += 1
            if j == s:
                return False
    return True


def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False


def ith_prime(i):
    'i番目の素数を返す.'
    for j, p in enumerate(prime_iter()):
        if j == i - 1 :
            return p


def primes(n):
    'n以下の素数のリストを返す.リストのinは遅いので注意.'
    s = [True] * n
    for x in range(2, int(n ** 0.5) + 1):
        if s[x]:
            mark(s, x)
    return [i for i in range(0, n) if s[i] and i > 1]


def prime_set(n):
    'n以下の素数のsetを返す.ある範囲で素数判定を何度もやりたい時に有効'
    return set(primes(n))


def prime_iter():
    '素数のジェネレータ. 無限に生成できるが遅い.'
    g = itertools.count(2)
    while True:
        prime = next(g)
        yield prime
        g = filter(lambda x, prime=prime: x % prime, g)


def prime_factors(n):
    'nの素因数のsetを返す. 定数回しか呼ばないときに有効.'
    if is_prime(n):
        return {n}
    ans = set()
    for p in primes(n):
        if n % p == 0:
            ans.add(p)
            n = n // p
    return ans


def phi(n, factors):
    'nとnの素因数factorsに対し, オイラーのφ関数φ(n)を計算する.'
    numer = 1
    denom = 1
    for p in factors:
        numer *= (p - 1)
        denom *= p
    return (numer * n) // denom


class Primes:
    '''Primes クラス.　1<=n<=max_ までの範囲の素数判定・素因数列挙・素数列挙を
        高速に行う. 範囲を超える数に対しては例外を発生させる.
    for文で範囲内の全素数に対して回すことも可能.
    '''

    def __init__(self, max_=10 ** 6):
        self.max_ = max_
        self.primes = primes(max_)
        self.primes_set = set(self.primes)
        self.exception = Exception('Range exceeded')

    def is_prime(self, n):
        '素数判定'
        if n > self.max_:
            raise self.exception
        return n in self.primes_set

    def __contains__(self, n):
        'Primes.is_prime(n) と等価.'
        return self.is_prime(n)

    def __iter__(self):
        'self._maxまでの素数のイテレータ'
        return (p for p in self.primes)

    def prime_factors(self, n):
        '素因数列挙'
        if n > self.max_:
            raise self.exception
        if self.is_prime(n):
            return {n}
        ans = set()
        for p in self.primes:
            if p > n:
                break
            if n % p == 0:
                ans.add(p)
                n = n // p
        return ans

    def ith_prime(self, i):
        'i番目の素数'
        if i > len(self.primes):
            raise self.exception
        else:
            return self.primes[i - 1]

if __name__ == '__main__':
    n = 2
    cont_frac = cont_frac_sqrt(n)
    for r in convergents(cont_frac):
        if abs(r - n ** 0.5) < 1e-10:
            break
        p = r.numerator
        q = r.denominator
        print(r, p / q, n ** 0.5 - p / q)
