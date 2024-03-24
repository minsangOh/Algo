import sys


def input(): return sys.stdin.readline()


n = int(input())
lst = list(map(int, input().split()))

start, end, result = 0, n - 1, 1e21

while start < end:
    Sum = lst[start] + lst[end]
    if abs(Sum) < abs(result):
        result = Sum
    if Sum < 0:
        start += 1
    else:
        end -= 1

print(result)
