import sys, heapq

input = sys.stdin.readline

point, line = map(int, input().split())
start = int(input())
arr = [[] for _ in range(point + 1)]
for _ in range(line):
    s, e, cost = map(int, input().split())
    arr[s].append((cost, e))

inf = int(12e12)
result = [inf] * (point + 1)


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    result[start] = 0

    while hq:
        sk, k = heapq.heappop(hq)

        if sk > result[k]:
            continue

        for lst in arr[k]:
            cost = sk + lst[0]
            if cost < result[lst[1]]:
                result[lst[1]] = cost
                heapq.heappush(hq, (cost, lst[1]))


dijkstra(start)
result.pop(0)
for i in range(len(result)):
    if result[i] == inf:
        result[i] = 'INF'
    print(result[i])
