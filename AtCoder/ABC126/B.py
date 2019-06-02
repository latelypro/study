s=input()

yy=int(s[:2])
mm=int(s[2:])

if yy <= 12 and mm <= 12 and yy != 0 and mm != 0:
    print('AMBIGUOUS')
elif mm <= 12 and mm != 0:
    print('YYMM')
elif yy <= 12 and yy != 0:
    print('MMYY')
else:
    print('NA')