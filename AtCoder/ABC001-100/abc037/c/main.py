#!/usr/bin/env python3
from itertools import product, permutations, combinations
N, K=map(int, input().split())
An=list(map(int, input().split()))
result = [0 for i in range(N-K+1)]
result[0] = sum(An[0:K])
for i in range(1, N-K+1):
    result[i] = result[i-1] - An[i-1] + An[i + K - 1]

print(sum(result))