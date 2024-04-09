import sys
from collections import deque, defaultdict


def input(): return sys.stdin.readline()


student, length = map(int, input().split())
lst = [(input())for _ in range(length)]

dic = defaultdict()

for number in lst:
    if number in dic:
        dic.pop(number)
        dic[number] = 1
    else:
        dic[number] = 1


for idx, key in enumerate(dic.keys()):
    if idx == student: break
    print(key, end='')
