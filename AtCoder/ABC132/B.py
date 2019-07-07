n=int(input())
p=list(map(int, input().split()))
cnt=0
for i in range (n):
    if i == 0:
        continue
    if i == n - 1:
        break
    if p[i-1] <= p[i] and p[i] <= p[i+1] or p[i+1] <= p[i] and p[i] <= p[i-1]:
        cnt+=1

print(cnt)