from collections import deque

def fun(s):
  tmp=deque([])
  for i in s:
    if i == "[" or i =="(":
      tmp.append(i)
    if i == "]" or i ==")":
      if len(tmp)>0 and tmp[-1] == ("[" if i=="]" else "("):
        tmp.pop()
      else:
        return "no"
  return "yes" if len(tmp)==0 else "no"

while True:
    a = input()

    if a==".":
        break
    print(fun(a))