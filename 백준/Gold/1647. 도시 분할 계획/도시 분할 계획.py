def find_bs(A):
    global arr
    if arr[A] == 0:
        return A
    ret = find_bs(arr[A])
    arr[A] = ret
    return ret


def union(a, b, cost):
    global arr, total, cnt, cost_lst
    fa, fb = find_bs(a), find_bs(b)
    if fa == fb:
        return
    total += cost
    cost_lst.append(cost)
    cnt += 1
    arr[fb] = fa


n, m = map(int, input().split())
lst = []
cost_lst =[]
for i in range(m):
    lst.append(list(map(int, input().split())))
lst.sort(key=lambda x: (x[2], x[0]))
arr = [0] * (n+1)
cnt = 0
total = 0

for i in range(m):
    x, y, price = lst[i]
    union(x, y, price)
print(total-cost_lst[-1])
