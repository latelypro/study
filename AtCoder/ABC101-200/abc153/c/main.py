#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N, K=map(int, input().split())
HP=sorted(list(map(int, input().split())), reverse=True)
cnt = 0
for i in range(N):
    if K > 0:
        K -= 1
        continue
    cnt += HP[i]

print(cnt)