import sys
def input(): return sys.stdin.readline()

m = int(input())
S = 0

for _ in range(m):
    lst = input().split()
    if len(lst) == 1:
        if lst[0] == 'all': S = (1 << 21) - 1
        else: S = 0
    else:
        st, x = lst[0], int(lst[1])
        if st == 'add': S |= (1 << x)
        elif st == 'remove': S &= ~(1 << x)
        elif st == 'check':
            if S & (1 << x):
                print(1)
            else:
                print(0)
        elif st == 'toggle':S ^= (1 << x)
