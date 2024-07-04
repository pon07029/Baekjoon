import sys  
a, b= map(int, input().split())
re=[]
for i in range(a):
  c = int(sys.stdin.readline())
  re.append(c)

s=1
l=max(re)
while l>=s:
  mid = (s+l)//2
  n=0
  for i in re:
    n+=i//mid
  if n < b:
    l=mid-1
  else:
    s=mid+1

print(l)