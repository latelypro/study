s=input()

odd='R'
even='L'

for i, item in enumerate(s):
    if (i+1) % 2 == 0:
        if item == 'R':
            print('No')
            break
    else:
        if item == 'L':
            print('No')
            break
else:
    print('Yes')