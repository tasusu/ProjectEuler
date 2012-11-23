'''
The primes 3, 7, 109, and 673, are quite remarkable.
By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109,
both 7109 and 1097 are prime. The sum of these four primes, 792,
represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes
concatenate to produce another prime.
'''

from collections import defaultdict
from intlib import is_prime_rand
import itertools
import intlib

def is_pair(p, q):
    a = int(str(p) + str(q))
    b = int(str(q) + str(p))
    return is_prime_rand(a) and is_prime_rand(b)

def is_clique(tpl, adj):
    for p, q in itertools.combinations(tpl, 2):
        if not q in adj[p]: return False
    return True

def main(max_ = 30000):
    # 各素数に対応する点の次数を管理して、次数が5未満の点は切り捨てたほうが良いかも.
    ans = []
    primes = intlib.primes(max_)
    adj = defaultdict(set)
    
    for p in primes:
        for q in (q for q in primes if q > p):
            if is_pair(p, q):
                adj[p].add(q)
                adj[q].add(p)
    
    adj = {p: s for p, s in adj.items() if len(adj[p]) > 4} #次数4以下の点を削除
    adj = {p: {q for q in ls if q in adj} for p, ls in adj.items()} #枝を更新
    print(len(adj), sum((len(s) for s in adj.values()))/len(adj))
    
    keys = sorted(adj.keys())
    ans = float('inf')
    for p in keys:
        if p > ans: break # pが暫定解を超えたら終了
        adj_p = sorted([x for x in adj[p] if x > p])
        for q in adj_p:
            if len(adj[p] & adj[q]) < 3: continue #pとqの共通隣接点は3個以上必要
            common_adj = sorted([x for x in adj[p] & adj[q] if x > q])
            for r, s, t in itertools.combinations(common_adj, 3):
                tpl = (p, q, r, s, t)
                if is_clique(tpl, adj):
                    print(tpl, sum(tpl))
                    ans = min((ans, sum(tpl)))
    
    if ans < max_: return ans #答えが確定する場合に返す
    
if __name__ == '__main__':
    import time
    t1 = time.time()
    print(main())
    t2 = time.time()
    print('{:.3f} s'.format(t2-t1))