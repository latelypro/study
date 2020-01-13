n=int(input())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c=list(map(int, input().split()))

sum=0
for i in range(0, n):
    ai = a[i] - 1
    if i != 0:
        if a[i] - a[i-1] == 1:
            sum += b[ai] + c[a[i-1]-1]
        else:
            sum += b[ai]
    else:
        sum += b[ai]

print(sum)