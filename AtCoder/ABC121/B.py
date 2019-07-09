n,m,c=map(int, input().split())
b = list(map(int, input().split()))
src_a = [0]*n
for i in range(n):
    src_a[i] = list(map(int, input().split()))

cnt=0
for a in src_a:
    sum=0
    for j in range(m):
        sum+=b[j]*a[j]
    if sum + c > 0:
        cnt+=1
print(cnt)
