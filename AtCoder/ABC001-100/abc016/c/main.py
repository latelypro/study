#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF=float('inf')
N, M=map(int, input().split())
dp = [[0 for i in range(N)] for j in range(N)]

for i in range(M):
    A, B=map(int, input().split())
    A, B = A-1, B-1
    dp[A][B] = 1
    dp[B][A] = 1

for i in range(N):
    ret = set()
    for j in range(N):
        # 友達じゃない
        if dp[i][j] == 0:
            continue
        for k in range(N):
            # 自分自身または友達は除外
            if k in (i, j):
                continue
            # 友達の友達
            if dp[i][k] == 0 and dp[j][k] == 1:
                ret.add(k)
    print(len(ret))

