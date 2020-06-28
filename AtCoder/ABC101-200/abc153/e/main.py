#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

H, N=map(int, input().split())
dp = [0 for i in range(H + 10**4 + 1)]

hm = list(list(map(int, input().split())) for i in range(N))

for i in range(1, H+1):
    dp[i] = min(list(dp[i - h] + m for h, m in hm))
print(dp[H])