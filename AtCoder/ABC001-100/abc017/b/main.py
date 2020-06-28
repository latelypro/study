#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left

X=input()
choku = ['c', 'h', 'o', 'k', 'u']
is_c = False
for s in X:
    if s in choku:
        if s == 'h':
            if not is_c:
                print('NO')
                exit()
            else:
                is_c = False
        
        if is_c:
            print('NO')
            exit()
            
        if s == 'c':
            is_c = True
        else:
            is_c = False

    else:
        print('NO')
        exit()
print('YES')