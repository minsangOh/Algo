n = int(input())
lst =(list(map(int, input().split())))
Max = max(lst)

for i in range(n):
    lst[i] = lst[i]*100/Max
print(sum(lst)/n)