#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
N=int(input())
A=sorted(list(map(int, input().split())))
B=sorted(list(map(int, input().split())))
C=sorted(list(map(int, input().split())))


ret = 0
for i in range(N):
    # 中段を決めた時、その値より小さくなる上段を探す
    new_A = bisect_left(A, B[i])
    # 中段を決めた時、その値より大きくなる下段を探す
    new_C = bisect_right(C, B[i])
    # 組み合わせ
    ret += new_A * (N - new_C)

print(ret)