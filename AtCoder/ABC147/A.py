a,b,c = map(int, input().split())
sum=a+b+c

if sum > 21:
    print('bust')
else:
    print('win')