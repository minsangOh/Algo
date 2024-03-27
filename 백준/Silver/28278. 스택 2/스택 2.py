import sys
def input(): return sys.stdin.readline()

stack = []

n = int(input())

for _ in range(n):

    lst = input().split()

    if lst[0] == '1':
        stack.append(lst[1])
    elif lst[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif lst[0] == '3':
        print(len(stack))
    elif lst[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    elif lst[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)