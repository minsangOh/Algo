import sys

input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    x, y, pt = map(int, input().split())
    arr = [[0] * x for _ in range(y)]
    used = [[0] * x for _ in range(y)]
    for _ in range(pt):
        xx, yy = map(int, input().split())
        arr[yy][xx] = 1
    q = deque()
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


    def bfs(y1, x1):
        global x, y, cnt
        cnt += 1
        q.append([y1, x1])
        while q:
            yy, xx = q.popleft()
            for i in range(4):
                ny, nx = yy + dy[i], xx + dx[i]
                if 0 <= nx < x and 0 <= ny < y and arr[ny][nx]==1:
                    if used[ny][nx] !=0: continue
                    used[ny][nx] = 1
                    q.append([ny,nx])

    cnt = 0
    for yyy in range(y):
        for xxx in range(x):
            if arr[yyy][xxx] == 1 and used[yyy][xxx]==0:
                bfs(yyy,xxx)
    print(cnt)


