from collections import defaultdict

def dfs(n):
    if n == 0: return 1
    if seq[n]: return seq[n]
    seq[n] = dfs(n // p) + dfs( n // q); return seq[n]

n, p, q = map(int, input().split()); seq = defaultdict(int); print(dfs(n))