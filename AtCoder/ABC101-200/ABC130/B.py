n,x=map(int,input().split())
l=list(map(int, input().split()))
d=0
dlist=[]
dlist.append(0)
for i in range(1,n+1):
    d=d+l[i-1]
    if d <= x:
        dlist.append(d)
print(len(dlist))
