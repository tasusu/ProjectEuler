'''
https://projecteuler.net/problem=61
'''

from collections import defaultdict
import itertools

def P(i, n):
    if i == 3: return n * (n + 1) // 2
    if i == 4: return n ** 2
    if i == 5: return n * (3 * n - 1) // 2
    if i == 6: return n * (2 * n - 1)
    if i == 7: return n * (5 * n - 3) // 2
    if i == 8: return n * (3 * n - 2)
    raise Exception(i)

# Global Variables
four_digit_values = defaultdict(list)
for i in range(3, 9):
    n = 1
    while P(i, n) < 10000:
        if P(i, n) >= 1000:
            four_digit_values[i].append(str(P(i,n)))
        n += 1

def color(n):
    return {i for i in range(3, 9) if n in four_digit_values[i]}

def six_cycles(nodes, adj):
    ans = set()
    for p in nodes:
        for q in adj[p]:
            for r in adj[q]:
                for s in adj[r]:
                    for t in adj[s]:
                        for u in adj[t]:
                            if p in adj[u] and len({p,q,r,s,t,u}) == 6:
                                ans.add((p,q,r,s,t,u))
    return ans

def colorable(cycle):
    p,q,r,s,t,u = cycle
    for tpl in itertools.product(color(p), color(q), color(r),
                                 color(s), color(t), color(u)):
        if set(tpl) == {3,4,5,6,7,8}: return True
    return False
    
def main():
    nodes = []
    for i in range(3, 9):
        nodes += four_digit_values[i]
    
    adj = defaultdict(set)
    for n in nodes:
        adj[n] = {m for m in nodes if n != m and n[2:] == m[:2]}
    
    print(len(nodes)) #頂点数
    print(sum((len(adj[n]) for n in nodes))/len(nodes)) #平均次数
    
    for cycle in six_cycles(nodes, adj):
        if colorable(cycle):
            return sum((int(p) for p in cycle))

if __name__ == '__main__':
#test
#    for i in range(3,9):
#        print([P(i,n) for n in range(1,6)])
    print(main())