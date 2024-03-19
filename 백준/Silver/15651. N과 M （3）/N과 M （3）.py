import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [i for i in range(1, n + 1)]
path = [0] * m


def recursive(lv):
    if lv == m:
        for i in range(lv):
            print(path[i], end=' ')
        print()
        return

    for i in range(n):
        path[lv] = lst[i]
        recursive(lv+1)

recursive(0)