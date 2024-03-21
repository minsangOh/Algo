import sys

input = sys.stdin.readline

lst = input().split('-')
Sum = 0

lst_1 = map(int, lst[0].split('+'))
Sum += sum(lst_1)

for group in lst[1:]:
    lstt = map(int, group.split('+'))
    Sum -= sum(lstt)

print(Sum)
