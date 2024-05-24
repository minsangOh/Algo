import sys
from collections import deque


def input(): return sys.stdin.readline()


n = int(input())
m = int(input())
lst = list(map(int, input().split()))

bucket = {}
queue = deque()

for i in lst:
    if i in bucket:
        bucket[i] += 1
    else:
        if len(queue) >= n:
            min_value = min(bucket.values())
            for num in queue:
                if bucket[num] == min_value:
                    del bucket[num]
                    queue.remove(num)
                    break
        bucket[i] = 1
        queue.append(i)

print(' '.join(map(str, sorted(queue))))
