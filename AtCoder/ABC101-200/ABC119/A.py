import datetime
s=input()

input_date = datetime.datetime.strptime(s, "%Y/%m/%d")
heisei = datetime.datetime(2019,4,30)

if input_date <= heisei:
    print('Heisei')
else:
    print('TBD')