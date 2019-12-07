n=int(input())
an=list(map(int, input().split()))

toukou =[]
for i,a in enumerate(an):
    toukou.append([str(i+1),str(a)])
toukou.sort(key=lambda x:int(x[1]))
number = []
for s in toukou:
    number.append(s[0])
print(' '.join(number))