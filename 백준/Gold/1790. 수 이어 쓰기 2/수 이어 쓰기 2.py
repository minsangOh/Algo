import sys, math
def input(): return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
cnt = 0
for i in range(1, n+1):
    cnt += (int(math.log(i, 10)) + 1)
    if cnt >= k:
        lst = list(str(i))
        break

if cnt == k:
    print(lst[-1])
elif cnt > k:
    print(lst[-(cnt-k)-1])
else:
    print(-1)