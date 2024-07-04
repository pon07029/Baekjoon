a, b= map(int, input().split())
li=[]
for i in range(a):
    k = input()
    li.append(k)

li2 =[]

def fun(e,f):
  c=0
  d=0
  
  for i in range(e,e+8):
    for j in range(f,f+8):
      if (i+j)%2 ==0:
        c += 0 if li[i][j]=="W" else 1
      else :
        c += 1 if li[i][j]=="W" else 0

  for i in range(e,e+8):
    for j in range(f,f+8):
      if (i+j)%2 ==1:
        d += 0 if li[i][j]=="W" else 1
      else :
        d += 1 if li[i][j]=="W" else 0
  
  return c if c<d else  d

for i in range(a-7):
  for j in range(b-7):
    li2.append(fun(i,j))

print(min(li2))