import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.floor(n**0.5)) + 1):
        if n % i == 0:
            return False
    return True

def max_gen_prime(a, b):
    i = 0
    while is_prime(i ** 2 + a * i + b):
        i = i + 1
    return i

if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(4))
    print(is_prime(100))
    print(max_gen_prime(-1,2))
    print(max_gen_prime(1, 41))
    print(max_gen_prime(-79, 1601))
    _max = 0
    result = (0, 0)
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            tmp = max_gen_prime(a, b)
            if _max < tmp:
                result = (a, b)
                _max = tmp
    a, b = result
    print(a, b)
    print(a * b)