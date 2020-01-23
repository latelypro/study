#!/usr/bin/env python3
items=list(map(int, input().split()))
K=int(input())
max_index = items.index(max(items))
for i in range(K):
    items[max_index] = items[max_index] * 2

print(sum(items))
    