n,k=map(int, input().split())
h=list(map(int, input().split()))
h.sort(reverse=True)
cnt = 0
for height in h:
    if height < k:
        break
    cnt+=1
print(cnt)