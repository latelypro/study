n=int(input())
sum=0

for i in range(n):
    value,unit=map(str, input().split())
    if unit == 'BTC':
        sum += float(value) * 380000
    else:
        sum+=float(value)
print(sum)