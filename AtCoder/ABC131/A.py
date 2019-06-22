s=input()
import re
p = '00'
for i in range(1, 11):
  if p in s:
      print('Bad')
      break
  p = str(i * 11)
else:
    print('Good')
