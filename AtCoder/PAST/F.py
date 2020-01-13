S=input()
str_list = []
word = ''
count = 0

for i in range(len(S)):
    if S[i].isupper():
        count += 1
        word = word + S[i]
        if count > 1:
            str_list.append(word)
            word = ''
            count = 0
    else:
        word = word + S[i]
str_list=sorted(str_list, key=str.lower)
print(''.join(str_list))
