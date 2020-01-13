N=int(input())
items=list(map(int, input().split()))

count = 1
break_num = 0

for item in items:
    if item == count:
        count += 1
    else:
        break_num += 1

if count == 1:
    print(-1)
else:
    print(break_num)
