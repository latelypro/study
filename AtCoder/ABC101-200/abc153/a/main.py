#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

H, A=map(int, input().split())
if H % A == 0:
    print(H//A)
else:
    print(H//A + 1)