N=int(input())
words=[input() for i in range(N)]

judge='Yes'
for index, word in enumerate(words):
    if index == 0:
        continue
    if word[0] != words[index-1][-1]:
        judge = 'No'
        break
    if words.count(word) > 1:
        judge = 'No'
        break

print(judge)