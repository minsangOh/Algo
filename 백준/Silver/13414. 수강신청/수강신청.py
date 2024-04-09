import sys


def input(): return sys.stdin.readline()


student, length = map(int, input().split())

dic = {}

for _ in range(length):
    number = input()
    if number in dic:
        del dic[number]
    dic[number] = True

for idx, key in enumerate(dic.keys()):
    if idx == student: break
    print(key, end='')
