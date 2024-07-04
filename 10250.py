import math
a = int(input())
re=[]
for i in range(a):
  a, b, c= map(int, input().split())
  d=c%a
  if c%a ==0:
    d=a
  re.append(f"{d}{str(math.ceil(c/a)).zfill(2)}")

for i in re:
  print(i)