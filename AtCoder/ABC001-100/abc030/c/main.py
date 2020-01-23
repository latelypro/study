#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

N, M=map(int, input().split())
X, Y=map(int, input().split())
An=list(map(int, input().split()))
Bn=list(map(int, input().split()))
now = 0
cnt = 0
for i in range(N):
    
    ret = bisect_left(An, now)
    if ret == N:
        break
    if now <= An[ret]:
        now = An[ret]
        now += X


    ret = bisect_left(Bn, now)
    if ret == M:
        break

    if now <= Bn[ret]:
        now = Bn[ret]
        now += Y
        cnt += 1
print(cnt)