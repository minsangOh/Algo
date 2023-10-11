import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

dy = [0, 0, 0, 1, -1]
dx = [0, 1, -1, 0, 0]
rotate = {1: [3, 4], 2: [3, 4], 3: [1, 2], 4: [1, 2]}
col, row = map(int, input().split())
arr = [[1] * (row + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(col)] + [
    [1] * (row + 2)]
sy, sx, st = map(int, input().split())
ey, ex, et = map(int, input().split())
cnt = 0
used = [[[0] * 5 for _ in range(row + 1)] for _ in range(col + 1)]
used[sy][sx][st] = 1
q = deque()
q.append([sy, sx, st, cnt])
while q:
    y, x, tilt, cnt = q.popleft()
    if y == ey and x == ex and tilt == et:
        print(cnt)
        break
    for k in range(1, 4):
        ny = y + (dy[tilt] * k)
        nx = x + (dx[tilt] * k)
        if 1 <= ny <= col and 1 <= nx <= row:
            if arr[ny][nx] == 1: break
            if used[ny][nx][tilt] == 0:
                used[ny][nx][tilt] = 1
                q.append([ny, nx, tilt, cnt + 1])
    for next_head in rotate[tilt]:
        if used[y][x][next_head] == 0:
            used[y][x][next_head] = 1
            q.append([y, x, next_head, cnt + 1])
