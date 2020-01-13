n=int(input())
h=list(map(int, input().split()))

count = [0] * (n+1)

for i in range(1,n):
    if h[i-1] >= h[i]:
        count[i] = count[i-1] + 1
    else:
        count[i] = 0
print(max(count))