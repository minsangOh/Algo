import sys
def input(): return sys.stdin.readline().rstrip()
dp = [0]*1000001
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, 1000001):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009
T = int(input())
for TC in range(1,T+1):
    n = int(input())
    print(dp[n])