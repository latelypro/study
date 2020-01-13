N,K,M=map(int, input().split())
An=list(map(int, input().split()))

result = M*N - sum(An)

if result < 0:
    print(0)
elif result <= K:
    print(result)
else:
    print(-1)