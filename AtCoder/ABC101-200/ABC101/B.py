N=input()
sn = 0
for n in N:
    sn += int(n)

if int(N) % sn == 0:
    print('Yes')
else:
    print('No')