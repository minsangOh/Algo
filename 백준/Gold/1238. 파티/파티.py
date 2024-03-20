import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start, graph, n):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance


n, m, t = map(int, input().split())

lst = [[] for _ in range(n + 1)]
R_lst = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    R_lst[b].append((a, c))

result_1 = dijkstra(t, lst, n)
result_2 = dijkstra(t, R_lst, n)

Max = 0
for i in range(1, n + 1):
    if result_1[i] + result_2[i] > Max:
        Max = result_1[i] + result_2[i]

print(Max)
