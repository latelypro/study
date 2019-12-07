n=int(input())
an=list(map(int,input().split()))
sum=0
for a in an:
    sum += 1/a
print(1/sum)