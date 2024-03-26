import sys


def input(): return sys.stdin.readline()


n = int(input())
bucket = set()
for _ in range(n):
    name, flag = input().split()
    if flag == 'enter':
        bucket.add(name)
    else:
        bucket.discard(name)


for i in sorted(bucket, reverse=True):
    print(i)

