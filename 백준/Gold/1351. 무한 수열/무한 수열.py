from collections import defaultdict

def dfs(n):
    if n == 0: return 1
    # dict는 키가 없으면 에러가 발생하는데
    # defaultdict를 쓰면 키값이 없으면 자체생성
    # 속도는 dict보다 느림
    # 백트래킹 때문에 사용
    if seq[n]: return seq[n] 

    seq[n] = dfs(n // p) + dfs( n // q); return seq[n]

n, p, q = map(int, input().split()); seq = defaultdict(int); print(dfs(n))