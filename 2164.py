from collections import deque
a = int(input())
li = deque([])
for i in range(a):
  li.append(i+1)
while len(li)>2:
  li.popleft()
  li.rotate(-1)
  
print(li[0] if len(li)==1 else li[1])