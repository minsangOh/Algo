import sys


def input(): return sys.stdin.readline()


n, m = map(int, input().split())
lst = list(map(int, input().split()))

start, end, Sum, cnt = 0, 0, 0, 0

while 1:
    if Sum >= m:
        Sum -= lst[start]
        start += 1
    elif end == n: break
    else:
        Sum += lst[end]
        end += 1

    if Sum == m: cnt += 1
        
print(cnt)
