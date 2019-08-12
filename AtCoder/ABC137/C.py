n=int(input())
sdict={}
cnt=0
for i in range(n):
    s=''.join(sorted(input()))
    if s in sdict:
        sdict[s] += 1
        cnt += sdict[s] - 1
    else:
        sdict[s] = 1
print(cnt)