N,K,Q=map(int, input().split())
results=[0 for i in range(N)]
for i in range(Q):
    index = int(input()) - 1
    results[index] += 1

for point in results:
    if (Q - K + 1) <= point:
        print('Yes')
    else:
        print('No')