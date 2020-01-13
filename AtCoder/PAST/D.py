N=int(input())
counter = [0] * N

for i in range(N):
    num = int(input())
    counter[num-1] += 1

max_count = max(counter)
min_count = min(counter)
if max_count == min_count:
    print('Correct')
else:
    print('{0} {1}'.format((counter.index(max_count)+1), (counter.index(min_count)+1)))