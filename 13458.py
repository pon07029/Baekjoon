import sys
z= int(sys.stdin.readline())
dat = list(map(int, sys.stdin.readline().split()))  
a, b = map(int, sys.stdin.readline().split())
sum=0
for i in dat:
    sum+=1
    if i>a:
      if (i-a)%b == 0:
         sum+= (i-a)//b
      else:
          sum+= (i-a)//b+1
print(sum)
