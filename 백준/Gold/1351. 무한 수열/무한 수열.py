import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


def dfs(n):
    if n == 0: return 1
    if seq[n]: return seq[n]

    div1 = n // p
    div2 = n // q

    seq[n] = dfs(div1) + dfs(div2)
    return seq[n]


n, p, q = map(int, input().split())
seq = defaultdict(int)

print(dfs(n))