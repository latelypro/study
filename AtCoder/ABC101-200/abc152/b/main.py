#!/usr/bin/env python3
from itertools import product, permutations, combinations
from bisect import bisect_right,bisect_left
a,b=map(str, input().split())
ab = ''.join([a for i in range(int(b))])
ba = ''.join([b for i in range(int(a))])
print(sorted([ab, ba]).pop(0))