N,M=map(int, input().split())
results = [[0,0] for i in range(N)]
wa=0
ac=0
for i in range(M):
    P,S=map(str, input().split())
    P = int(P) - 1
    if S == 'AC':
        if results[P][0] == 0:
            wa += results[P][1]
            results[P][1] = 0
            ac += 1
            results[P][0] += 1
    else:
        results[P][1] += 1

print("{0} {1}".format(ac,wa))