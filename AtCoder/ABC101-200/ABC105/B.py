N=int(input())

is_buy = 'No'
for a in range((N//4)+1):
    for b in range((N//7)+1):
        if 4*a + 7*b == N:
            is_buy = 'Yes'
            break
print(is_buy)