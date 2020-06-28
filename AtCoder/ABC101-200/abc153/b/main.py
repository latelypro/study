#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

H, N=map(int, input().split())
An=sorted(list(map(int, input().split())), reverse=True)
for a in An:
    H -= a

if H <= 0:
    print('Yes')
else:
    print('No')
    