N=int(input())

from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 9)
@lru_cache(maxsize=None)
def nfib(n):
    if n < 2:
        return 1
    else:
        return n * nfib(n-2)

cnt = 0
for s in str(nfib(N)):
    if s == '0':
        cnt += 1
    else:
        cnt = 0
print(cnt)