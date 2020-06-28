#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N=int(input())
dp = [[0 for i in range(3)] for j in range(N)]
h=[list(map(int, input().split())) for i in range(N)]
for i in range(N):
    if i == 0:
        dp[0] = h[0]
        continue
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+h[i][j])
print(max(dp[-1]))
