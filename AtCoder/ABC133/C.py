L,R=map(int, input().split())
n=R-L
ans=[]
if n == 1:
    print((L*R)%2019)
elif n < 2019:
    for i in range(n+1):
        for j in range(1,n+1):
            l=L+i
            r=l+j
            if r > R:
                break
            ans.append((l*r) % 2019)
    print(min(ans))
else:
    print(0)

