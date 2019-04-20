const=998244353

def is_triangle(r,g,b):
    max = max[r,g,b]

    if max < r+g+b-max:
        return True
    return False


