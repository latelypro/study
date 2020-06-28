#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N, K=map(int, input().split())
Pn=list(map(int, input().split()))
V = [0] * N
ans = [0] * K
max_v = 0
sum_v = 0
for n in range(N):
    V[n] = (0.5*Pn[n]*(Pn[n]+1))/Pn[n]
    if n < K:
        sum_v += V[n]
        max_v = sum_v
    else:
        sum_v = sum_v - V[n-K] + V[n]
        max_v = max(max_v, sum_v)
print(max_v)