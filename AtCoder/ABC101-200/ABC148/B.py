N=int(input())
S,T=map(str, input().split())

new = ""
for i in range(N):
    new += S[i] + T[i]

print(new) 