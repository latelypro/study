N=int(input())
from itertools import combinations

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

import math 
n=int(math.sqrt(N))
k=n
divisors = []
if (n ** 2) == N:
    k = 2 * (n-1)
else:
    divisors = make_divisors(N)
    center = (len(divisors) // 2) - 1
    k = divisors[center] - 1 + divisors[center+1] - 1

print(k)



