from collections import deque

a = int(input())
re=deque([])
for i in range(a):
  b = int(input())
  re.append(b) if b!=0 else re.pop() 

print(sum(re))