w,h,x,y=map(int, input().split()) 

if w == h:
    if x==w/2 and y==h/2:
        print(w*h*0.5, 1)
    else:
        print(w*h*0.5, 0)
else:
    if x==w/2 and y==h/2:
        print(w*h*0.5, 1)
    else:
        print(w*h*0.5, 0)