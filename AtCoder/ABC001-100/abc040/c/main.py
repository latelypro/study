#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N=int(input())
an=list(map(int, input().split()))
dp = [0 for i in range(N+2)]
dp[1] = abs(an[1] - an[0])
for i in range(2, N):
    dp[i] = min(dp[i-2] + abs(an[i-2] - an[i]), dp[i-1] + abs(an[i] - an[i-1]))
print(dp[N-1])