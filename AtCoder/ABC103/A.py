items=list(map(int, input().split()))
m=sum(items)-(max(items)+min(items))
print(abs(max(items)-m)+ abs(min(items)-m))