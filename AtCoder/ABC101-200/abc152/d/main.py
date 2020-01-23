#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

N=int(input())

tbl = [[0] * 10 for i in range(10)]

for i in range(1, N+1):
    num = str(i)
    s = int(num[0])
    e = int(num[-1])
    tbl[s][e] += 1

cnt = 0
for i in range(10):
    for j in range(10):
        cnt += tbl[i][j] * tbl[j][i]
print(cnt)