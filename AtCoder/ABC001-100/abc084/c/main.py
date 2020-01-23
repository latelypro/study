#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

N=int(input())
times = [list(map(int, input().split())) for i in range(N-1)]
for start in range(N-1):
    current = start + 1
    elapsed =  times[start][1] + times[start][0]
    while current < N-1:
        if elapsed < times[current][1]:
            elapsed = times[current][1]
        if elapsed % times[current][2] != 0:
            elapsed = times[current][2] * (elapsed // times[current][2] + 1)
        elapsed += times[current][0] 
        current += 1
    print(elapsed)
print(0)



