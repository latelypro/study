n,k=map(int,input().split())
a=list(map(int,input().split()))

count=0
for i in range(n):
    for j in reversed(range(i+1, n+1)):
        s=sum(a[i:j])
        if s>=k:
            count+=1
        else:
            break
print(count)
