#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N=int(input())
Pn=list(map(int, input().split()))
dp = [[False for i in range(10**4+1)] for j in range(N+1)]

dp[0][0] = True
for i in range(N):
    for j in range(10**4+1):
        if j - Pn[i] >= 0:
            if dp[i][j-Pn[i]]:
                dp[i+1][j] = True
        if dp[i][j]:
            dp[i+1][j] = True

ans = 0
for i in range(10**4+1):
    if dp[N][i]:
        ans += 1
print(ans)