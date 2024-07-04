import math
a = int(input())
re=[]
  

for i in range(a):
  b = int(input())
  c = int(input())
  sum = 0
  for j in range(1, c+1):
    sum += math.comb(j+b-2, j-1)*(c-j+1)
  re.append(sum)
for i in re:
  print(i)