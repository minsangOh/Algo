import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [input() for _ in range(n)]
cnt = int(12e12)

for y in range(n - 7):
    for x in range(m - 7):
        cnt_1 = 0
        cnt_2 = 0
        for yy in range(y, y + 8):
            for xx in range(x, x + 8):
                if (yy + xx) % 2 == 0:
                    if arr[yy][xx] == arr[y][x]:
                        cnt_1 += 1
                    else:
                        cnt_2 += 1
                else:
                    if arr[yy][xx] != arr[y][x]:
                        cnt_1 += 1
                    else:
                        cnt_2 += 1
        cnt = min(cnt_1, cnt_2, cnt)

print(cnt)
