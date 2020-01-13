N,K=map(int, input().split())
An=list(map(int, input().split()))
from itertools import combinations
S=list(combinations(An, K))
result = 0
mod = 10 ** 9 + 7
for s in S:
    f = max(s) - min(s)
    result += f

print(result % mod)
