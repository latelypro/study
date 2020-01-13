n=int(input())
alist=[int(input()) for i in range(n)]
b=sorted(alist, reverse=True)
for a in alist:
    if a < b[0]:
        print(b[0])
    elif b[0] <= a:
        print(b[1])