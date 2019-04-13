bottuns=list(map(int, input().split())) 
coins=0
for i in range(2):
    index = bottuns.index(max(bottuns))
    coins += bottuns[index]
    bottuns[index] = bottuns[index] - 1

print(coins)