a = int(input())
re=[]
for i in range(a):
  b = input()
  re.append(len(b))

for i in re:
  print("yes" if i>5 and i <10 else "no")