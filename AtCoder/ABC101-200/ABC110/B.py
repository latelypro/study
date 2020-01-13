N,M,X,Y=map(int, input().split())
Xpoints=list(map(int, input().split()))
Ypoints=list(map(int, input().split()))
isWar='War'
for z in range(-99, 101):
    if X < z and z <= Y:
        if max(Xpoints) < z:
            if min(Ypoints) >= z:
                isWar = 'No War'
                break

print(isWar)
