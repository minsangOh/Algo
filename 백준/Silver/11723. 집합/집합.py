import sys


def input(): return sys.stdin.readline()


m = int(input())
S = 0

for _ in range(m):
    lst = input().split()
    if len(lst) == 1:
        if lst[0] == 'all':
            S = (1 << 21) - 1  # 21의 비트 생성 후 1로 초기화
        else:
            S = 0
    else:
        st, x = lst[0], int(lst[1])
        if st == 'add':
            S |= (1 << x)  # x 비트에 1 설정(or 연산자)
        elif st == 'remove':
            S &= ~(1 << x)  # x 비트에 0 설정 (and, not 연산자)
        elif st == 'check':
            if S & (1 << x):  # S의 x번째에 있으면 1 출력
                print(1)
            else:
                print(0)
        elif st == 'toggle':
            S ^= (1 << x)  # x 비트 반전 (Xor 연산자)