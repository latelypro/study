S=input()
T=input()

match='No'
for i in range(len(S)):
    end=S[-1]
    change = end + S[0:len(S)-1]
    if T == change:
        match='Yes'
    else:
        S=change

print(match)
