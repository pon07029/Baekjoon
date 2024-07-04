import sys
a, b = map(int, sys.stdin.readline().split())
d=0
e=0
re=[]
for i in range(a):
  c= sys.stdin.readline()
  re.append(c)

for i in re:
  if "X" not in i:
    d+=1
for i in range(b):
  c=""
  for j in range(a):
    c+=re[j][i]
  if "X" not in c:
    e+=1
print(max(d,e))
    
  
