from itertools import permutations, combinations
n=int(input())
num_per_min = [int(input()) for i in range(5)]
point = [n,0,0,0,0,0]
time = 0
while(True):
    zero_over_index = sorted([i for i in range(len(point)) if point[i] >0], reverse=True)
    for index in zero_over_index:
      if index != 5:
        if point[index] >= num_per_min[index]:
          point[index] = point[index] - num_per_min[index]
          point[index+1] = point[index+1] + num_per_min[index]
        else:
          point[index+1] = point[index+1] + point[index]
          point[index] = 0
    time+=1
    if point[5] == n:
        print(time)
        break