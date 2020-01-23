#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

A,B,C,D=map(int, input().split())

t= B / A
a = D / C

if a > t :
    print("AOKI")
elif a == t:
    print('DRAW')
else:
    print('TAKAHASHI')