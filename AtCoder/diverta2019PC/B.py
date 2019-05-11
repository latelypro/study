R,G,B,N=map(int, input().split())
cnt=0
import math
r_range=math.ceil(N/R)+1
g_range=math.ceil(N/G)+1
for r in range(r_range):
    red = r*R
    for g in range(g_range):
        rem = (N-red-g*G)
        mod = rem % B
        if rem>=0 and mod == 0:
            cnt+=1
print(cnt)