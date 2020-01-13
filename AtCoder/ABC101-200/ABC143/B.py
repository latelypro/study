n=int(input())
d_i=list(map(int, input().split()))

import itertools
cmb_d = list(itertools.combinations(d_i, 2))

sum =0
for cmb in cmb_d:
  sum += cmb[0] * cmb[1]

print(sum)