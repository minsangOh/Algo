import sys

n = int(sys.stdin.readline())

room, cnt = 1, 1
while n > room: room += 6 * cnt; cnt += 1
print(cnt)
