#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N,X=map(int, input().split())
M=[int(input()) for i in range(N)]
Y = X - sum(M)

cnt = N
cnt += (Y // min(M))
print(cnt)