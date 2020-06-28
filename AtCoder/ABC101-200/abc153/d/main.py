#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

H=int(input())
cnt = 1
p = 1
import math
while H > 1:
    H = math.floor(H/2)
    cnt += 2 ** p
    p += 1
print(cnt)