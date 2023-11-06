import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
lst = sorted([int(input()) for _ in range(n)])
xy = []

# x+y+z = k  -->   x+y = k-z
for i in range(n):
    for j in range(i, n):
        xy.append(lst[j] + lst[i])
xy.sort()

Max = 0
for i in range(n):
    for j in range(i, n):
        zk = lst[j] - lst[i]    # x+y+z = k  -->   x+y = k-z
        s = 0
        e = len(xy) - 1
        while s <= e:
            mid = (s + e) // 2
            new = xy[mid]
            if zk > new:
                s = mid + 1
            elif zk < new:
                e = mid - 1
            else:
                Max = max(Max, lst[j])
                break
print(Max)
