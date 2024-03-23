import sys
def input(): return sys.stdin.readline()


m = int(input())
S = set()

for _ in range(m):
    lst = input().split()
    if len(lst) == 1:
        if lst[0] == 'all':
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        st, x = lst[0], int(lst[1])
        if st == "add":
            S.add(x)
        elif st == "remove":
            S.discard(x)
        elif st == "check":
            if x in S:
                print(1)
            else:
                print(0)
        elif st == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
