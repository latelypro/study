H,W=map(int, input().split())
h,w=map(int, input().split())

s = H * W 
b1 = h * W
b2 = w * (H - h)

print(s - b1 - b2)
