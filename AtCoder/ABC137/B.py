k,x=map(int,input().split())
a=[]
for i in range(-k+1,k):
    a.append(x+i)
print(" ".join(map(str,a)))