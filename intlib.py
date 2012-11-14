import math

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
    yield 2
    prime_ls = [2]
    n = 3
    while True:
        flag = True
        for p in prime_ls:
            if p > int(math.floor(n**0.5)) + 1: break
            if n % p == 0:
                flag = False
                break
        if flag:
            yield n
            prime_ls.append(n)
        n += 2
    
def is_pandigit(s):
    '文字列sがpandigitかどうか調べる.'
    if len(s) != 9: return False
    s = set([a for a in s if a != '0'])
    return len(s) == 9

def is_square(x):
    'xが平方数か調べる.'
    if x < 0: return False
    return math.floor(math.sqrt(x))**2 == x
    
if __name__ == '__main__':
    print(is_prime(97))
    print(is_prime(13*17))
    print(primes(10**3))
    for i, p in enumerate(prime_iter()):
        if i > 10: break
        print(p)