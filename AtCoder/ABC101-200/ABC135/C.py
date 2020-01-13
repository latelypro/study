n=int(input())
monsters=list(map(int, input().split()))
battle=list(map(int, input().split()))
remain=0
win=0
for i in range(n):
    if monsters[i] < battle[i]:
        win += monsters[i]
        if monsters[i+1] >= battle[i] - monsters[i]:
            win += battle[i] - monsters[i]
            monsters[i+1] -= battle[i] - monsters[i]
        else:
            win += monsters[i+1]
            monsters[i+1] = 0
    else:
        win += battle[i]
print(win)