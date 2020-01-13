n=int(input())

an = []
for i in range (0, n):
    an.append(int(input()))

    if i != 0:
        if an[i] == an[i-1]:
            print('stay')
        elif an[i] < an[i-1]:
            diff = an[i-1] - an[i]
            print('down {0}'.format(diff))
        else:
            diff = an[i] - an[i-1]
            print('up {0}'.format(diff))
