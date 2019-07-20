n=int(input())
lines=list(map(int, input().split()))
max_line=max(lines)
sum=sum(lines) -max_line
if sum > max_line:
    print('Yes')
else:
    print('No')