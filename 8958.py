a = int(input())
re=[]
for i in range(a):
  su=0
  b = input()
  li = b.split("X")
  for j in li:
    su+=(len(j)*(len(j)+1)//2)
  re.append(su)

for i in re:
  print(i)