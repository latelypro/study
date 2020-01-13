s=input()

num = 'error'

try:
    num = int(s)
except:
    print(num)
else:
    print(num * 2)