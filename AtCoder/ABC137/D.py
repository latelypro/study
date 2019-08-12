n,m=map(int,input().split())
job=[list() for i in range(n)]
days = [0] * n
values = [0] * n
dp = [[0] * 100000] * 100000
for i in range(n):
    a,b=map(int, input().split())
    days[i] = a
    values[i] = b 

for j in range(n):
    for k in range(1,m+1):
        if m-k >= days[i]:
            dp[j+1][m] = max([dp[j][m-days[i]]+values[i], dp[j][m]])
        else:
            dp[j+1][m] = dp[j][m] 

print(dp[n][m])