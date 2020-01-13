a,b,x = map(int, input().split())

start = 0
end = 10 ** 9 +1

while end - start > 1:
    n=(start + end) //2
    if a * n + b * len(str(n)) <= x:
        start = n
    else:
        end = n
print(start)

