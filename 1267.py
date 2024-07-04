a=0
b=0
int(input())
dat = list(map(int, input().split()))

for i in dat:
  a+=i//30+1
  b+=i//60+1
a*=10
b*=15
if a<b:
  print('Y',a)
elif a>b:
  print('M',b)
else:
  print('Y M',a)