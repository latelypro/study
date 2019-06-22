N,L=map(int, input().split())
aji=[i+L-1 for i in range(1,N+1)]
org=sum(aji)
aji_list=[]
for i in aji:
    aji_list.append([abs(i),org-i])

print(min(aji_list)[1])