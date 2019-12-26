A,B,C,D=map(int, input().split())
dx=C-A
dy=D-B
print(C-dy, D+dx, C-dy-dx, D+dx-dy)
