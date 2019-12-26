A,B=map(int, input().split())

import fractions
def lcm(a,b):
    return (a*b) // fractions.gcd(a,b)

print(lcm(A,B))