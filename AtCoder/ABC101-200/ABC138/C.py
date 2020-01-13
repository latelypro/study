n=int(input())
vn=list(map(int,input().split()))
vn=sorted(vn)
value=0
for i in range(n-1):
    if i == 0:
        value = (vn[0] + vn[1])/2
    else:
        value = (value + vn[i+1])/2
print(value)