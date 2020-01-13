n,k=map(int,input().split())
s=input()
s=[bool(int(s[i])) for i in range(n)]
true_index_list=[]
for i in range(k):
    true_index_list =[]
    for state_index in range(len(s)):
        if s[state_index] is True:
            true_index_list.append(state_index)
    if len(true_index_list) == 0:
        for false_index in range(n):
            s[false_index] = not s[false_index]
    elif len(true_index_list) == 1:
        for false_index in range(true_index_list[0]):
            s[false_index] = not s[false_index]
    else:
        start = 0
        end = 0
        diff = 0
        for index in range(len(true_index_list)):
            if index == len(true_index_list) - 1:
                break
            if true_index_list[index+1] - true_index_list[index] >= diff:
                start = true_index_list[index]
                end = true_index_list[index+1] 
                diff =  true_index_list[index+1] - true_index_list[index]
        for false_index in range(start+1, end):
            s[false_index] = not s[false_index]

cnt=0
max_cnt = 0
for state in s:
    if state:
        cnt+=1
    else:
        max_cnt = cnt
        cnt = 0


if cnt >= max_cnt:
  max_cnt = cnt
print(max_cnt)

