'''
Develop a method to express Roman numerals in minimal form.
'''

import re


def num_to_roman(n):
    '''
    自然数nを表すローマ数字文字列を返す.
    16 -> 'XVI' (10 + 5 + 1)
    19 -> 'XIV'10 + 9
    91 -> ''
    '''
    ans = ''

    # 1000 = Mをできるだけ書く
    ans += 'M' * (n // 1000)
    n = n % 1000

    # CMが使える場合は使う
    if n >= 900:
        ans += 'CM'
        n = n - 900
    # 500 以上ならDを書く
    elif n >= 500:
        ans += 'D'
        n = n - 500
    # CDが使える場合は使う
    elif n >= 400:
        ans += 'CD'
        n = n - 400
    # Cをできるだけ書く
    ans += 'C' * (n // 100)
    n = n % 100

    # 10-99までの処理
    if n >= 90:
        ans += 'XC'
        n = n - 90
    elif n >= 50:
        ans += 'L'
        n = n - 50
    elif n >= 40:
        ans += 'XL'
        n = n - 40
    ans += 'X' * (n // 10)
    n = n % 10

    # 1-9までの数の処理
    if n == 9:
        ans += 'IX'
        n = 0
    elif n >= 5:
        ans += 'V'
        n = n - 5
    elif n == 4:
        ans += 'IV'
        n = 0
    ans += 'I' * n

    return ans


ROMAN_REG = re.compile('^(M*)((?:CM)*)(D*)((?:CD)*)(C*)((?:XC)*)(L*)\
((?:XL)*)(X*)((?:IX)*)(V*)((?:IV)*)(I*)$')
ROMAN_MAGNITUDES = [1000, 450, 500, 200, 100, 45, 50, 20, 10, 4.5, 5, 2, 1]


def roman_to_num(s):
    '''
    ローマ数字文字列sが表す自然数nを返す.
    roman_to_num('IIIIIIIIIIIIIIII') = 16
    roman_to_num('VIIIIIIIIIII')     = 16
    roman_to_num('VVIIIIII')         = 16
    '''
    groups = ROMAN_REG.match(s).groups()
    return int(sum((len(groups[i]) * ROMAN_MAGNITUDES[i]
                for i in range(13))))


def main():
    ans = 0
    for line in open('src/roman.txt', 'r', encoding='utf-8'):
        s = line.rstrip()
        min_s = num_to_roman(roman_to_num(s))

        # TEST
        if roman_to_num(s) != roman_to_num(min_s):
            raise Exception(s, min_s)
        if len(s) < len(min_s):
            raise Exception(s, min_s)

        ans += len(s) - len(min_s)
    return ans

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
