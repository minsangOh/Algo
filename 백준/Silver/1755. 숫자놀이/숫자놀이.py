import sys

def input():
    return sys.stdin.readline()

m, n = map(int, input().split())

lst = []

st = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for i in range(m, n + 1):
    word = []
    for j in str(i):
        word.append(st[int(j)])
    res = " ".join(word)
    lst.append((i, res))

lst.sort(key=lambda x: x[1])

cnt = 0
for num, _ in lst:
    if cnt > 0 and cnt % 10 == 0:
        print()
    print(num, end=" ")
    cnt += 1
