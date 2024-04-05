import sys


def input(): return sys.stdin.readline()


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
for lst in arr:
    Max_gcd = -9e31
    loop = len(lst)
    for i in range(loop):
        for j in range(i+1, loop):
            res = GCD(lst[i], lst[j])
            if Max_gcd < res: Max_gcd = res
    print(Max_gcd)
