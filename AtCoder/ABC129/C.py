N, M=map(int, input().split())
mod=10**9+7
dp=[0 for i in range(N+2)]
dp[N] = 1
is_broken =[False for i in range(N+1)]

for i in range(M):
    a=int(input())
    is_broken[a] = True

for i in reversed(range(N)):
    if is_broken[i]:
        dp[i] = 0
        continue
    dp[i] = (dp[i+1] + dp[i+2]) % mod

print(dp[0])
    