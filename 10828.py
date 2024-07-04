import sys
a = int(input())
re=[]
stack =[]

def fun(s):
  if s[0]=="push":
    stack.append(s[1])
  elif s[0]=="pop":
    if len(stack) ==0:
      print(-1)
    else:
      print(stack.pop())
  elif s[0]=="size":
    print(len(stack))
  elif s[0]=="empty":
    print(1 if len(stack)==0 else 0)
  else:
    print(-1 if len(stack)==0 else stack[-1])


for i in range(a):
  b = list(map(str, sys.stdin.readline().split()))
  fun(b)

