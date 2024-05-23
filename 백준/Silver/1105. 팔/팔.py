import sys

input = sys.stdin.readline

l, r = input().rstrip().split()
cnt = 0
if len(l) != len(r):
    print(0)
else:
    for x in range(len(l)):
        if l[x] == r[x]:
            if l[x] == '8':
                cnt += 1
        else: break
    print(cnt)