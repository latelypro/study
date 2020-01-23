#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

N=int(input())
Pn=list(map(int, input().split()))
p_min = [10**5 + 7 for i in range(N+1)]

cnt = 1
p_min[0] = Pn[0]
for i in range(1, N):
    p_i = Pn[i]
    p_j = min(p_i, p_min[i-1])
    p_min[i] = p_j
    if p_i <= p_j:
        cnt += 1
print(cnt)