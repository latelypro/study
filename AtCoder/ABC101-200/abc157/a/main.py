#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N=int(input())
if N % 2 == 0:
    print(N//2)
else:
    print(N//2 + 1)