s = int(input())
def f(x):
  if x % 2 == 0:
    return x/2
  else:
    return 3 * x + 1

X = [s]
m = 1
next = s

while True:
  m += 1
  next = f(next)
  if next in X:
    break
  else:
    X.append(next)
    
print(m)
