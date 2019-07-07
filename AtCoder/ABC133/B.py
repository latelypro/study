n,d=map(int,input().split())
x=[[0]*d]*n
for i in range(n):
    x[i]=list(map(int, input().split()))
import math
cnt=0
for i, p in enumerate(x):
    for q in range(i+1, n):
        dist=0
        sum=0
        for j in range(d):
            sum+=(p[j]-x[q][j])**2
        dist=math.sqrt(sum)
        if dist.is_integer():
            cnt+=1
print(cnt)
