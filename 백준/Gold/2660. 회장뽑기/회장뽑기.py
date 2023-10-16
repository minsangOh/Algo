"""
23 / 10 / 16 알고 스터디
회장뽑기
"""
import heapq
import sys
def input(): return sys.stdin.readline().rstrip()

from collections import defaultdict, deque

n = int(input())
friendship = defaultdict(list)
while 1:
    person1, person2 = map(int, input().split())
    if person1 == person2 == -1: break
    friendship[person1].append(person2)
    friendship[person2].append(person1)

result = defaultdict(int)

for i in range(1, n+1):
    used = [0]*(n+1)
    used[i] = 1
    now = [i, 0]
    q = deque()
    q.append(now)
    while q:
        friend, cost = q.popleft()
        for value in friendship[friend]:
            if used[value] != 0: continue
            q.append([value, cost+1])
            used[value] = cost+1
        result[i] = max(used)

ans = min(result.values())
lst =[]

for key, value in result.items():
    if value == ans:
        lst.append(key)

print(ans, len(lst))
print(*lst)
