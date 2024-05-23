import sys
from itertools import combinations

input = sys.stdin.readline

n, target = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    arr = combinations(lst, i)
    for lstt in arr:
        if sum(lstt) == target:
            cnt += 1

print(cnt)
