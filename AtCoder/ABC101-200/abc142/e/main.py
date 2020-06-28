#!/usr/bin/env python3
n, m = map(int, input().split())
dp = [float('inf')] * 2**n
dp[0] = 0
for _ in range(m):
    a, _ = map(int, input().split())
    c = sum([2**(int(i)-1) for i in input().split()])
    for s in range(2**n):
            t = s|c
            if dp[t] > dp[s] + a:
                dp[t] = dp[s] + a
ans = dp[-1]
if ans == float('inf'):
    ans = -1
print(ans)
