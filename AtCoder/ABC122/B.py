s=input()
max=0
cnt=0
for _ in s:
    if _ in ['A','G','T','C']:
        cnt+=1
        if max < cnt:
            max = cnt
    else:
        cnt=0
print(max)