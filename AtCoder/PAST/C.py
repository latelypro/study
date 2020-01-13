numbers = list(map(int, input().split()))

for i in range(2):
    max_index = numbers.index(max(numbers))
    numbers.pop(max_index)
print(max(numbers))