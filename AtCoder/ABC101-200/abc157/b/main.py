#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
INF = float('inf')

card=[list(map(int, input().split())) for i in range(3)]
N=int(input())
num=[int(input()) for i in range(N)]
for i in range(3):
    for j in range(3):
        if card[i][j] in num:
            card[i][j] = True
        else:
            card[i][j] = False

res = 'No'
for i in range(3):
    if all(card[i]):
        res = 'Yes'
    if card[0][i] == card[1][i] == card[2][i] == True:
        res = 'Yes'

if card[0][0] == card[1][1] == card[2][2] == True:
    res = 'Yes'
elif card[0][2] == card[1][1] == card[2][0] == True:
    res = 'Yes'
print(res)
