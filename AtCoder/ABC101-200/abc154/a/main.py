#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

S,T=map(str, input().split())
A,B=map(int, input().split())
U=str(input())
if U == S:
    print(A-1, B)
else:
    print(A, B-1)