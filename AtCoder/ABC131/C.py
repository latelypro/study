a,b,c,d=map(int, input().split())
count = 0
num=b-a+1
import fractions
lcm= int(c*d / fractions.gcd(c,d))
ac=(a-1)//c
ad=(a-1)//d
acd=(a-1)//lcm

bc=b//c
bd=b//d
bcd=b//lcm

print(num-((bc+bd-bcd)-(ac+ad-acd)))