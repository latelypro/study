#!/usr/bin/env python3
from itertools import product, permutations, combinations
N=int(input())
dp = [N for i in range(N+1)]
dp[0] = 0
for i in range(1, N+1):
    power = 1
    while power <= i:
        dp[i] = min(dp[i], dp[i-power] + 1)
        power *= 6
    power = 1
    while power <= i:
        dp[i] = min(dp[i], dp[i-power] + 1)
        power *= 9
print(dp[N])