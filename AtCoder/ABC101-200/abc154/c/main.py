#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

N=int(input())
An=list(map(int, input().split()))
def has_duplicates(seq):
    return len(seq) != len(set(seq))

if has_duplicates(An):
    print('NO')
else:
    print('YES')