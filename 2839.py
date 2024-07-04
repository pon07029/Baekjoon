a = int(input())
if a == 1 or a ==2 or a==4 or a==7 :
  print(-1)
else:
  r= a//5
  tmp = a%5
  while tmp !=0:
    if tmp%3==0:
      r+=tmp//3
      tmp=0
    else:
      tmp+=5
      r-=1

  print(r)
