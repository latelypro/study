n=int(input())
plist=list(map(int, input().split()))
k=0
for i in range(1,n+1):
    if i != plist[i-1]:
        k+=1
if k <= 2:
    print('YES')
else:
    print('NO')