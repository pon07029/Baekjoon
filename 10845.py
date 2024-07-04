import sys
from collections import deque

a = int(input())
stack =deque([])

def fun(s):
  if s[0]=="push":
    stack.append(s[1])
  elif s[0]=="pop":
    if len(stack) ==0:
      print(-1)
    else:
      print(stack.popleft())
  elif s[0]=="size":
    print(len(stack))
  elif s[0]=="empty":
    print(1 if len(stack)==0 else 0)
  elif s[0]=="front":

    print(-1 if len(stack)==0 else stack[0])
  else:
    print(-1 if len(stack)==0 else stack[-1])


for i in range(a):
  b = list(map(str, sys.stdin.readline().split()))
  fun(b)
