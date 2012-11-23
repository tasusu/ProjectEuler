'''
Problem 67
https://projecteuler.net/index.php?section=problems&id=67
'''

def main():
    s = open('src/triangle.txt').read()
    
    a = [[int(n) for n in line.split()] for line in s.splitlines()]
    d = [[0] * len(a) for j in range(len(a))]
    d[0][0] = a[0][0]
    
    for i in range(1, len(a)):
        for j in range(i + 1):
            tmp = []
            if j > 0:
                tmp.append(d[i - 1][j - 1])
            if j < i:
                tmp.append(d[i - 1][j])
            d[i][j] = a[i][j] + max(tmp)
    
    return max(d[-1])
    

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))