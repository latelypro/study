#!/usr/bin/env python3
from itertools import product, permutations, combinations
a,b=map(int, input().split())
tower=[0 for i in range(1000)]
tower[0] = 1

for i in range(1, 1000):
    tower[i] = tower[i-1] + (i + 1)
    diff_a = tower[i-1] - a
    diff_b = tower[i] - b
    if (diff_a == diff_b) and diff_a > 0 and diff_b > 0:
        print(diff_a)
        break
