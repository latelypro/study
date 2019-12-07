n=int(input())
alist=[int(input()) for i in range(n)]
for i in range(n):
    if i == 0:
        max_a = 0
    else:
        max_a = max(alist[0:i])
    if i == n-1:
        max_b = alist[-1]
    else:
        max_b = max(alist[i+1:])
    print(max([max_a, max_b]))