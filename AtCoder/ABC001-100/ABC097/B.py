import math
X = int(input())

sq = int(math.sqrt(X))

m = 1
for b in range(2, sq+1):
    p = 2
    tmp = b ** p
    while tmp <= X:
        m = max(tmp, m)
        p += 1
        tmp = b ** p

print(m)
