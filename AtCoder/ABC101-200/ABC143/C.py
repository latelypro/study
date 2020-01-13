n=int(input())
s=input()

last = []

for i in range(n):
    if i == n-1:
        last.append(s[i])
    else:
        if s[i] == s[i+1]:
            continue
        else:
            last.append(s[i])

print(len(last))
