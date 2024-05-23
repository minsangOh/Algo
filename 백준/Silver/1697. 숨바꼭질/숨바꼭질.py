from collections import deque

n, k = map(int, input().split())
if n == k:
    print(0)
    # print(0)

elif n > k:
    print(n-k)
    ans = n-k
    # for i in range(ans+1):
        # print(ans, end=' ')
        # ans -= 1


else:
    used = [0] * (2 * (k+1))
    q = deque()
    q.append(n)
    while q:
        n = q.popleft()
        dx = [-1, 1, n]
        for i in range(3):
            nn = n + dx[i]
            if 0 <= nn <= (1.5 * k):
                if used[nn] != 0:
                    continue
                used[nn] = used[n] + 1
                q.append(nn)
            if nn == k:
                print(used[nn])
                q = []
                break