'''
How many different ways can one hundred be written
as a sum of at least two positive integers?
'''

def main():
    MAX = 100
    pre_table = [1] * (MAX + 1)
    
    for k in range(2, MAX):
        table = [0] * (MAX + 1)
        for n in range(MAX + 1):
            table[n] = sum(pre_table[n - i * k] for i in
                           range(0, n//k + 1))
        pre_table = table
       
    return table[MAX]
    

if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))