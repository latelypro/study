#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')
na, nb = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


dp = [[0] * (nb + 1) for _ in range(na + 1)]
dp[na][nb]=0

for i in reversed(range(na+1)):
    for j in reversed(range(nb+1)):
        if i == na and j == nb:
            continue
        # 先攻
        if (i+j) % 2 == 0:
            if i == na:
                dp[i][j] = dp[i][j+1] + B[j]
            elif j == nb:
                dp[i][j] = dp[i+1][j] + A[i]
            else:
                dp[i][j] = max(dp[i+1][j] + A[i], dp[i][j+1]+B[j])
        else:
            if i == na:
                dp[i][j] = dp[i][j+1]
            elif j == nb:
                dp[i][j] = dp[i+1][j]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j+1])
print(dp[0][0])