#!/usr/bin/env python3
N, W=map(int, input().split())
WV=[list(map(int, input().split())) for i in range(N)]
dp = [-1] * (W+1)
dp[0] = 0
for w, v in WV:
    for i in range(W, w-1, -1):
        if dp[i-w] == -1:
            continue
        dp[i] = max(dp[i], dp[i-w] + v)
print(max(dp))
