n=int(input())
s=list(input())
cnt=0
for i in range(n):
    if i == 0:
        continue
    if s[i-1] == "#" and s[i] ==".":
        s[i] = "#"
        cnt+=1
print(cnt)
