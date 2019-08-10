n=int(input())
h=list(map(int,input().split()))
max=0
res='Yes'
for i in range(n):
    if i == n -1:
        break
    diff = h[i] - h[i+1]

    if max < h[i]:
        max=h[i]
        if diff == 1:
            max -= 1
    max_diff = max - h[i+1]
    #print(i, diff, max_diff)
    if  diff > 1 or max_diff > 0:
        res='No'
        break
    else:
        pass
print(res)