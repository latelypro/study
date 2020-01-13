n=int(input())
s=[]
for i in range(n):
    a=input().split()
    a.append(i+1)
    s.append(a)
print(s)
s=sorted(s, key=lambda x:(x[0],-x[1]))
print(s)
