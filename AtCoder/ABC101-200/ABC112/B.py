N,T=map(int, input().split())
costs = []

for i in range(N):
    cost, time = map(int, input().split())
    if time > T:
        continue
    else:
        costs.append(cost)
if len(costs) != 0:
    print(min(costs))
else:
    print('TLE')