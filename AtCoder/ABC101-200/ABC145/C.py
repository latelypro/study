N=int(input())
points=[input().split() for i in range(N)]
import math
def calc_dist(start, end):
    return math.sqrt((int(start[0]) - int(end[0])) ** 2 + (int(start[1]) - int(end[1])) ** 2)

from itertools import combinations, permutations
total_dist = []
for root in permutations(range(N), N):
    dist = 0
    for num in range(len(root)-1):
        dist += calc_dist(points[root[num]], points[root[num+1]])
    total_dist.append(dist)
from statistics import mean
print(mean(total_dist))


