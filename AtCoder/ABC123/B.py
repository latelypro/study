from  itertools import permutations
wait_time = [int(input()) for i in range(5)]
wait_time_p = list(permutations(wait_time))
min_total=643
for time_list in wait_time_p:
    total = 0
    for i in range(len(time_list)):
        total += time_list[i]
        if i == 4:
          break
        mod10 = total % 10
        if mod10 != 0:
            total += (10 - mod10)
    if total <= min_total:
        min_total = total
print(min_total) 