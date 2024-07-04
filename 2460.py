sum=0
top=0
for i in range(10):
  a, b= map(int, input().split())
  sum+=b-a
  if sum>top:
    top=sum
print(top)
