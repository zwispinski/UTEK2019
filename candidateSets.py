from itertools import chain, combinations
import numpy as np

def candidateSets(val, wt, cap):

    n = len(v)
    m = np.zeros([n, W+1])

    for i in range(1, n):
        for j in range(cap+1):
            if wt[i] > j:
                m[i, j] = m[i-1, j]
            else:
                m[i, j] = max(m[i-1, j], m[i-1, j-wt[i]] + val[i])

    sol = m[-1, -1]

    def all_subsets(ss):
        return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

    def isInTol(x, sol, tol):
        return (x <= sol and x >= sol-tol)

    tol = 10
    cand = list(filter(lambda x: isInTol(sum(x), sol, tol), all_subsets(val)))
    cand = [list(c) for c in cand]
    out = []
    for c in cand:
        out += [[v.index(x) for x in c]]
    return out

"""
v = [10, 20, 30, 50, 40]
w = [5, 40, 10, 20, 30]
W = 50

print candidateSets(v, w, W)
"""
