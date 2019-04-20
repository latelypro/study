a,b,c=map(int, input().split())  #複数数値入力

if a > b:
    if a > c and c > b:
        print("Yes")
    else:
        print("No")
else:
    if b > c and c > a:
        print("Yes")
    else:
        print("No")