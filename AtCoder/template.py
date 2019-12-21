a=int(input())  #数値入力
a,b=map(int, input().split()) #複数数値入力
c=list(map(int, input().split()))  #リスト入力
s=[list(map(int,list(input()))) for i in range(h)]  # 二次元配列入力
a=100
b=0.987654321
print('{0:06d}-{1:6f}'.format(a,b))  # 0埋め
# 000100-0.987654

print(*c)  #リスト出力
for i in [['#','.','#'],['#','#','#']]:print(*i, sep='') #二次元リストで間を詰めたもの
#.#
###

#内包表記奇数のみ
a=[i for i in range(100) if i%2==1]

#ソート
w=[[1, 2], [2, 6] , [3, 6], [4, 5], [5, 7]]
w.sort()
w.sort(key=lambda x:x[1],reverse=True)  #二個目の要素で降順並び替え

#素数リスト
n = 100
primes = set(range(2, n+1))
for i in range(2, int(n**0.5+1)):
    primes.difference_update(range(i*2, n+1, i))
primes=list(primes)

#二重ループ
n,y=1000, 1234000
for i in range(n+1):
    for j in range(n-i+1):
        if y-10000*i-5000*j==1000*(n-i-j):
            print(i, j, n-i-j)
            break
    else:
        continue
    break
else:
    print('-1 -1 -1')

#二部探索
import bisect
a = [1, 2, 3, 5, 6, 7, 8, 9]
b=bisect.bisect_left(a, 8)

#最大公約数、最小公倍数
import fractions
a,b=map(int, input().split())
f=fractions.gcd(a,b)
f2=a*b//f
print(f,f2)

#combinations、組み合わせ、順列
from itertools import permutations, combinations,combinations_with_replacement,product
a=['a','b','C']
print(list(permutations(a)))
print(list(combinations(a,2)))
print(list(combinations_with_replacement(a,3)))

#ビット演算、式を計算
a=list(product(['+','-'],repeat=3))
s=['5', '5', '3', '4']
for i in a:
    ans=s[0]+i[0]+s[1]+i[1]+s[2]+i[2]+s[3]
    if eval(ans)==7:
        print(ans+'=7')
        break

#集計
from collections import Counter
a=[2,2,2,3,4,3,1,2,1,3,1,2,1,2,2,1,2,1]
a=Counter(a)
for i in a.most_common(3):print(i)

#n進数
n=64
k=-3
bi=''
while n!=0:
    bi+=str(n%abs(k))
    if k<0:n=-(-n//k)
    else:n=n//k
print(bi[::-1])

 # 約数列挙
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

# 二重配列の要素でそーと
items = [[1,2],[2,3]]
sorted(items, key=lambda x: x[1])