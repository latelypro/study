#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N,M,X=map(int, input().split())
A=list(map(int, input().split()))
low = 0
high = 0
for a in A:
    if a < X:
        low += 1
    else:
        high += 1
print(min(low, high))