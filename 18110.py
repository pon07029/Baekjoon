import math
import sys
a = int(input())
re=[]

if a==0:
  print(0)
else:
  for i in range(a):
    b = int(sys.stdin.readline())
    re.append(b)

  re.sort()
  r = math.floor(a*0.15+0.5)
  sum = 0
  for i in range(r, len(re)-r):
    sum+=re[i]

  print(math.floor(sum/(len(re)-2*r)+0.5))