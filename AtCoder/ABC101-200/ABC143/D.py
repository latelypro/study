n=int(input())
L=list(map(int, input().split()))

def is_triangle(a, b, c):
    x = a - b
    y = a + b

    if x < c and -x < c and c < y:
        return True
    else:
        return False

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    ret = tuple(pool[i] for i in indices)
    if is_triangle(ret[0], ret[1], ret[2]):
        yield ret
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        ret2 = tuple(pool[i] for i in indices)
        if is_triangle(ret2[0], ret2[1], ret2[2]):
            yield ret2
print(len(list(combinations(L, 3))))