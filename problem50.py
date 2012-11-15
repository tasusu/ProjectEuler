'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to
a prime below one-hundred.

The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum
of the most consecutive primes?
'''

import intlib

if __name__ == '__main__':
    max_ = 1000000
    primes = intlib.Primes(max_)
    ans = 0 #こたえ
    max_len = 0 #連続和の最大長
    for p in primes:
        if p * max_len > max_: # p*max_len が上限を超えた時点で探索終了.
            break
        s = p # pからはじまる素数和
        for i, q in enumerate((q for q in primes if q > p)):
            s+= q
            if s > max_: break
            if primes.is_prime(s) and i + 2 > max_len:
                ans = s
                max_len = i + 2
    print(ans, max_len)
                