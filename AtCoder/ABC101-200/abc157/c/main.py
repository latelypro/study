#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')
N, M=map(int, input().split())
num=['0' for i in range(N)]
res = True
kv={}
for i in range(M):
    s,c=map(str, input().split())
    if s in kv:
        if kv[s] != c:
            print(-1)
            exit()
    else:
        kv[s] = c
if len(kv) > 0:
    for k, v in kv.items():
        num[int(k)-1] = v
    ret_str = ''
    is_first = True
    for n in num:
        if n == '0':
            if is_first:
                continue
            else:
                ret_str += n
        else:
            is_first = False
            ret_str += n

    if len(ret_str) == N:
        print(ret_str)
    else:
        print(-1)
else:
    print(-1)