'''
By analysing a user's login attempts, can you determine the
secret numeric passcode?
'''

import itertools


def check_password(password, attempt):
    'passwordがattemptに整合するかをチェック'
    a, b, c = tuple(attempt)
    lo = password.find(a)
    hi = len(password) - password[::-1].find(c)
    if lo < 0 or hi > len(password):
        return False
    for i in range(lo, hi):
        if password[i] == b:
            return True
    return False


def main():
    with open('src/keylog.txt', 'r', encoding='utf-8') as f:
        attempts = [row.rstrip() for row in f]

    for length in itertools.count(8):
        for tpl in itertools.product('01236789', repeat=length):
            password = ''.join(tpl)
            if all((check_password(password, attempt)
                    for attempt in attempts)):
                return password

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
