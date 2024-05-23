arr = [[1] * 10] + [[1] + ([0] * 8) + [1] for _ in range(8)] + [[1] * 10]

king, stone, move = input().split()
king = list(king)
king[0] = ord(king[0]) - 64
king[1] = int(king[1])

stone = list(stone)
stone[0] = ord(stone[0]) - 64
stone[1] = int(stone[1])

move = int(move)
dy = [0, 1, 1, 1, 0, -1, -1, -1]
dx = [1, 1, 0, -1, -1, -1, 0, 1]
direction = ['R', 'RT', 'T', 'LT', 'L', 'LB', 'B', 'RB']
for i in range(move):
    direction_name = input()
    pt = direction.index(direction_name)
    ny = king[1] + dy[pt]
    nx = king[0] + dx[pt]
    if arr[ny][nx] == 1:
        continue
    if ny == stone[1] and nx == stone[0] and  arr[stone[0] + dx[pt]][stone[1] + dy[pt]] == 1:
        continue
    king[0] = nx
    king[1] = ny
    if king[0] == stone[0] and king[1] == stone[1]:
        stone[0] += dx[pt]
        stone[1] += dy[pt]
print(f'{chr(king[0] + 64)}{king[1]}')
print(f'{chr(stone[0] + 64)}{stone[1]}')
