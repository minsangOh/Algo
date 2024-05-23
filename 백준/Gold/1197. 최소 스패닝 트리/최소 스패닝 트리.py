import sys

input = sys.stdin.readline


def find_bs(A):
    if bs[A] == 0:
        return A
    ret = find_bs(bs[A])
    bs[A] = ret
    return ret


def union(a, b, cost):
    global mst_cost, cnt
    boss_a, boss_b = find_bs(a), find_bs(b)
    if boss_a == boss_b:
        return
    bs[boss_b] = boss_a
    mst_cost += cost
    cnt += 1


v, e = map(int, input().split())
mst_cost = 0
cnt = 0
bs = [0] * 10001
lst = [list(map(int, input().split())) for _ in range(e)]
lst.sort(key=lambda x: x[2])
for i in range(e):
    if cnt == v - 1:
        break
    a, b, cost = lst[i]
    union(a, b, cost)
print(mst_cost)
