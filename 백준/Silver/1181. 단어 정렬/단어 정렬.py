import sys

n = int(input())
arr = [sys.stdin.readline().rstrip() for _ in range(n)]
arr = set(arr)
arr = sorted(arr, key=lambda x: (len(x), x))
for lst in arr:
    print(lst)
