n=int(input())
an=list(map(int, input().split()))
sum = 0
for i in range(0, n-1):
    for j in range(i+1, n):
        sum += an[i] ^ an[j]

print(sum % (10**9 + 7))
