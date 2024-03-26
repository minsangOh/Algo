import sys


def input(): return sys.stdin.readline()


n = int(input())
bucket = {}
lst = []
for _ in range(n):
    name, flag = input().split()
    bucket[name] = flag

for name, flag in bucket.items():
    if flag == 'enter':
        lst.append(name)

reverse_lst = reversed(sorted(lst))

for i in reverse_lst:
    print(i)

