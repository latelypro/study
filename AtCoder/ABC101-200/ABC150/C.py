N=int(input())
Pn=tuple(map(int, input().split()))
Qn=tuple(map(int, input().split()))
a,b=0,0

from itertools import permutations
seq = [i for i in range(1, N+1)]
for i, l in enumerate(list(permutations(seq))):
    if l == Pn:
        a = i
    if l == Qn:
        b = i

print(abs(a-b))