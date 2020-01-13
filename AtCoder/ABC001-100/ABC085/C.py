N,Y=map(int, input().split())
result = ["-1","-1","-1"]
for i in range(N+1):
    for j in range(N-i+1):
        k = N - (i + j) 
        x = 10000 * i + 5000 * j + 1000 * k
        if Y == x:
            result = [str(i), str(j), str(k)]
            break
print(" ".join(result))
