from collections import deque
import sys
a = int(input())

def fun(l):
  tmp=[]
  m=0
  re=deque([])
  for i in l:
    if len(re)==0 or re[-1]<i:
      for j in range(m+1, i+1):
        re.append(j)
        tmp.append("+")
      m=i
    if re[-1]== i:
      re.pop()
      tmp.append("-")
    else:
      return ["NO"]
  return tmp  

re=[]
for i in range(a):
  b = int(sys.stdin.readline())
  re.append(b)

lll= fun(re)
for i in lll:
  print(i)