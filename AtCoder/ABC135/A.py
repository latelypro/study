a,b=map(int, input().split())
k=(a+b)/2
print(k)
if not isinstance(k, int):
    print('IMPOSSIBLE')
else:
    print(int(k))