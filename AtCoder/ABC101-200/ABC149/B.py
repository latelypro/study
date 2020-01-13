A,B,K=map(int, input().split())

if A - K >= 0:
    print(str(A-K) + " " + str(B))
else:
    if B-(K-A) < 0:
        B = 0
    else:
        B = B-(K-A)
    print("0 " + str(B))
