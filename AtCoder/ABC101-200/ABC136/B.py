n=int(input())

res=0
if n < 10:
    res=n
elif 10 <= n and n < 10**2:
    res=9
elif 10**2 <= n and n < 10**3:
    res=9+(n-10**2)+1
elif 10**3 <= n and n < 10**4:
    res=9+900
elif 10**4 <= n and n < 10**5:
    res=9+900+(n-10**4)+1
elif n == 10**5:
    res = 9 + 900 + 90000
else:
    pass
print(res)