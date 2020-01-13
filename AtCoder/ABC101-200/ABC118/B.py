n,m=map(int, input().split())
cnt = [0]*m
for i in range(n):
    like = list(map(int, input().split()))
    k = like.pop(0)
    for j in like:
        cnt[j-1] += 1

all_like=0
for _ in cnt:
    if _ == n:
        all_like += 1
print(all_like)