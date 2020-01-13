s=input()

hug = 0
for i in range(0, len(s)//2):
    if s[i] != s[len(s)-1-i]:
        hug += 1

print(hug)
