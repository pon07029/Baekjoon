import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

def fun(s):
  tmp = 0
  for i in s:
    tmp += 1 if i =="(" else -1
    if tmp <0:
      return "NO"
  return "YES" if tmp ==0 else "NO"

for i in data:
  print(fun(i))