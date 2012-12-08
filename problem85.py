'''
Investigating the number of rectangles in a rectangular grid.
'''


def num_of_rect(h, l):
    '''h×lのマス目の小長方形の合計数'''
    return h * (h + 1) * l * (l + 1) // 4


def main():
    TARGET = 2000000
    current = 0
    ans = 0
    for l in range(1, int(TARGET ** 0.5)):
        for h in range(1, l + 1):
            if abs(num_of_rect(h, l) - current) < abs(TARGET - current):
                current = num_of_rect(h, l)
                ans = h * l

    return ans


if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2 - t1))
