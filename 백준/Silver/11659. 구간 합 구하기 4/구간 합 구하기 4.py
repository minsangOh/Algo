import sys


def input(): return sys.stdin.readline()


n, m = map(int, input().split())
lst = list(map(int, input().split()))
Sum_lst, Sum = [0], 0

for num in lst:
    Sum += num
    Sum_lst.append(Sum)

for _ in range(m):
    i, j = map(int, input().split())
    Sum = Sum_lst[j] - Sum_lst[i-1]
    print(Sum)
