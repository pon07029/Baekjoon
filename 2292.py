import math
a = int(input())
b=(a-2)//6

if a==1:
  print(1)
elif b==0:
  print(2)
else :
  for i in range(math.floor(math.sqrt(b)) , 100000):
    if b >= i*(i+1)//2 and b < (i+1)*(i+2)//2:
      print(i+2)
      break
