n,k=map(int,input().split())
INF=10**9+7
import math
all=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
cnt=0
for i in range(1,k):
    # 全順列
    all_p=math.factorial(n-k+i)/math.factorial(n-k)
    a=0
    if i!=1:
        # 連続する青とそれ以外の青のボールが隣り合う順列
        a = (math.factorial(n-k+1)/math.factorial(n-k)) * (math.factorial(i)/math.factorial(i-1))
    
    # 連続する青とそれ以外の青が隣合わない順列
    b = int(all_p - a)
    cnt+=b
    print(b % INF)
print(int(all-cnt)%INF)