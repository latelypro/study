#!/usr/bin/env python3
from itertools import product, permutations, combinations

H=2
W=int(input())
candies = [list(map(int, input().split())) for i in range(H)]

count = [0 for i in range(W)]

for p in range(W):
    count[p] = sum(candies[0][0:p+1]) + sum(candies[1][p:W+1])
print(max(count))

