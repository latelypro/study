#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
from collections import Counter
INF = float('inf')


N=int(input())
An=sorted(list(map(int, input().split())))
# 各要素の出現回数をカウント
C = Counter(An)
# 1回以上出現しているものを抽出
C = [(k ,v) for k, v in C.items() if v > 1]
if len(C) < 2:
    print(0)
else:
    C = sorted(C, key=lambda x:x[0])
    # 正方形
    if C[-1][1] >= 4:
        print(C[-1][0] ** 2)
    else:
        print(C[-1][0]*C[-2][0])