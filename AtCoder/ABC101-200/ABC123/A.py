antenas = [int(input()) for i in range(5)]
k = int(input())
for i in range(5):
    for j in range(5-i):
        if antenas[j] - antenas[i] > k:
            print(':(')
            break
    else:
        continue  
    break
else:
    print('Yay!')