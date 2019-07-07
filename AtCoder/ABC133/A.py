n,a,b=map(int, input().split())
train=n*a
taxi=b
if train <= taxi:
    print(train)
else:
    print(taxi)