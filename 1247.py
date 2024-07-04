import sys
li=[]
sum = 0
for i in range(int(input())):
  sum+= int(sys.stdin.readline())

if sum==0:
  li.append(0)
elif sum>0:
  li.append("+") 
else:
  li.append("-")

sum = 0
for i in range(int(input())):
  sum+= int(sys.stdin.readline())

if sum==0:
  li.append(0)
elif sum>0:
  li.append("+") 
else:
  li.append("-")

sum = 0
for i in range(int(input())):
  sum+= int(sys.stdin.readline())

if sum==0:
  li.append(0)
elif sum>0:
  li.append("+") 
else:
  li.append("-")

print(*li, sep="\n")