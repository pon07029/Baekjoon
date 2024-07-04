num=1
for i in range(int(input())):
  b, c= map(int, input().split())
  if b==num:
    num=c
  elif c==num:
    num=b

print(num) 

