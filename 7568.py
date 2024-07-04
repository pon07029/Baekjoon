a = int(input())
re=[]
for i in range(a):
  a, b= map(int, input().split())
  re.append([a,b])

def fun(c,d):
  k=0
  for i in re:
    if i[0] > c and i[1] >d:
      k+=1
  return k+1


for i in re:
  print(fun(i[0], i[1]), end=" ")
