n = int(input())
nn = abs(n)

dp =[0]*1000001
dp[1] = 1
for i in range(2, nn+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

if n > 0:
    print(1)
elif n == 0:
    print(0)
elif nn % 2 == 1:
    print(1)
else:
    print(-1)

print(dp[nn])