#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

n, m=map(int, input().split())
s = (30 * (n) + (0.5 * m)) % 360)
l = 6 * m

if s <= l:
    print(l - s)
else:
    print(s - l))
