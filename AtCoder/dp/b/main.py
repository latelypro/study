#!/usr/bin/env python3
N, K=map(int, input().split())
h=list(map(int, input().split()))
dp = [10**5] * N
dp[0] = 0
for i in range(1, N):
    x = max(0, i-K)
    dp[i] = min([dp[j]+abs(h[j]-h[i]) for j in range(x, i)])
print(dp[-1])