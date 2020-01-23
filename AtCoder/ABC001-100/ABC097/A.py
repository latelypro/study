A,B,C,D=map(int, input().split())


if abs(B-A)<=D and abs(C-B) <= D or abs(A-C) <= D:
    print('Yes')
else:
    print('No')