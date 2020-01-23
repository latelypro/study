#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

A,B=map(int, input().split())
S=input()
res = S.split('-')
if len(res) != 2:
    print('No')
else:
    if len(res[0]) == A and len(res[1]) == B:
        print('Yes')
    else:
        print('No')
