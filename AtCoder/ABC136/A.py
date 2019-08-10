a,b,c=map(int, input().split())
if b+c > a:
    print(c-(a-b))
else:
    print(0)