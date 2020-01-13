n=int(input())
h=list(map(int,input().split()))
tmp=h[0]
for i in range(1,n):
    if h[i] - tmp == 0:
        tmp = h[i]
    elif h[i] - tmp >= 1:
        tmp = h[i] -1
    else:
        print('No')
        exit()
print('Yes')