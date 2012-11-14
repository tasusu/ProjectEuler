def len_cycle(d):
    ls = []
    n = 1
    while True:
        n = n * 10
        if n % d == 0:
            return 0
        if n % d in ls:
            return len(ls)
        else:
            n = n % d
            ls.append(n)
            
    
if __name__ == '__main__':
    _max = 0
    for d in range(2, 1000):
        if _max < len_cycle(d):
            _max = d
    print(_max)