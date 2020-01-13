N=int(input())

score = []

for i in range(N-1):
    score = score + list(map(int, input().split()))

over_zero = [val for val in score if val > 0]

if len(over_zero) == 0:
    print(0)
else:
    print(sum(over_zero))
