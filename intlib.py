import math
import itertools
import random


'''
 素数関係ない関数
------------------------
'''

def sq_pow(a, power, mod):
    'modつきのべき乗を高速に行う'
    b = 1
    while power:
        if power & 1: #一番下のbitを見る
            b = b * a % mod
        power = power >> 1 #1ビットシフト
        a = a ** 2 % mod
    return b

def is_pandigit(s):
    '文字列sがpandigitかどうか調べる.'
    if len(s) != 9: return False
    s = set([a for a in s if a != '0'])
    return len(s) == 9

def is_square(x):
    'xが平方数か調べる.'
    if x < 0: return False
    return math.floor(math.sqrt(x))**2 == x

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
    for i in range(2, int(math.floor(n**0.5)) + 1):
        if n % i == 0:
            return False
    return True

def mark(s, x):
    for i in range(x + x, len(s), x):
        s[i] = False

def ith_prime(i):
    'i番目の素数を返す.'
    for j, p in enumerate(prime_iter()):
        if j == i - 1 : return p

def primes(n):
    'n以下の素数のリストを返す.リストのinは遅いので注意.'
    s = [True] * n
    for x in range(2, int(n**0.5) + 1):
        if s[x]: mark(s, x)
    return [i for i in range(0,n) if s[i] and i > 1]

def prime_set(n):
    'n以下の素数のsetを返す.ある範囲で素数判定を何度もやりたい時に有効'
    return set(primes(n))

def prime_iter():
    '素数のジェネレータ. 無限に生成できるが遅い.'
    g = itertools.count(2)
    while True:
        prime = next(g)
        yield prime
        g = filter(lambda x, prime = prime: x % prime, g)
    
def prime_factors(n):
    'nの素因数のsetを返す. 定数回しか呼ばないときに有効.'
    if is_prime(n): return {n}
    ans = set()
    for p in primes(n):
        if n % p == 0:
            ans.add(p)
            n = n // p
    return ans

'''
Primes クラス.
1<=n<=max_ までの範囲の素数判定・素因数列挙・素数列挙を
高速に行う. 範囲を超える数に対しては例外を発生させる.
for文で範囲内の全素数に対して回すことも可能.
--------------------------
'''

class Primes:
    def __init__(self, max_ = 10**6):
        self.max_ = max_
        self.primes = primes(max_)
        self.primes_set = set(self.primes)
        
    def is_prime(self, n):
        '素数判定'
        if n > self.max_ :
            raise Exception('Range exceeded')
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
            raise Exception('Range exceeded')
        if self.is_prime(n): return {n}
        ans = set()
        for p in self.primes:
            if p > n: break
            if n % p == 0:
                ans.add(p)
                n = n // p
        return ans
    
    def ith_prime(self, i):
        'i番目の素数'
        if i > len(self.primes):
            raise Exception('Range exceeded')
        else:
            return self.primes[i - 1]
        
        
'''
Miller-Rabin乱択素数判定
'''
       
def is_prime_rand(n, repeat = 5):
    if n == 2: return True
    if n == 1 or n % 2 == 0: return False
    d = n - 1
    s = 0
    while d & 1 == 0:
        s += 1
        d = d >> 1
    for i in range(repeat):
        a = random.randint(1, n - 1)
        y = sq_pow(a, d, n)
        if y != 1:
            j = 0
            while y != n - 1 and j < s:
                y = y * y % n
                j += 1
            if j == s: return False
    return True
    
if __name__ == '__main__':
    print(ith_prime(3))
    _max = 10**5
    import time
    t1 = time.time()
    s = 0
    for p in Primes(_max):
        s += p
    t2 = time.time()
    print(s)
    print('Primes: {}'.format(t2-t1))
    t1 = time.time()
    s = 0
    for p in prime_iter():
        if p > _max: break
        s += p
    t2 = time.time()
    print(s)
    print('Itertools: {}'.format(t2-t1))
    
    