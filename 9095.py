import sys
li=[]
for i in range(int(input())):
  a= int(sys.stdin.readline())
  li.append(a)
re =[]
for i in range(max(li)):
  if i == 0:
    re.append(1)
  elif i == 1:
    re.append(2)
  elif i == 2:
    re.append(4)
  else:
    re.append(re[i-1]+re[i-2]+re[i-3])

for i in li:
  print(re[i-1])