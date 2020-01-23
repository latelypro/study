#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

import math
n = 10**5
e = [True]*(n+1)
e[0] = False
e[1] = False
for i in range(2, int(n**0.5)+1):
    if not e[i]:
        continue
    for j in range(i*2, n+1, i):
        e[j] = False

c = [0]*(n+2)
for i in range(3, n+1, 2):
    if e[i] and e[(i+1)//2]:
        c[i] += 1

for i in range(3, n+1):
    c[i] += c[i-1]

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(c[r]-c[l-1])


