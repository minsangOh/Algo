n = int(input())
arr = list(map(int, input().split()))

result=[1]*n

for y in range(n):
    code = arr[y]
    for x in range(y):
        value = arr[x]
        if code > value:
            result[y] = max(result[x] + 1, result[y])
print(max(result))