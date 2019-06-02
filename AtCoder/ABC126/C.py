n,k=map(int, input().split())
p=0
import math
for i in range(1, n+1):
    if i < k/2:
        pi = math.ceil(math.log2(k/i))
        p += (1/n)*((0.5)**pi)
    elif i >= (k/2) and i < k:
        p += (1/n)*0.5
    else:
        p+= 1/n 

print(p)
