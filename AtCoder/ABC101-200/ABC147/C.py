n=int(input())

word_dict = {}
for i in range(0, n):
    word_num = int(input())
    words = [ list(map(int, input().split())) for j in (0, word_num)]
    word_dict[i] = words

max_true = 15

