s=input()
pre=bool(int(s[0]))
cnt=0
for i in range(1, len(s)):
    if pre == bool(int(s[i])):
        cnt+=1
        pre= not bool(int(s[i]))
    else:
        pre = bool(int(s[i]))
print(cnt)
