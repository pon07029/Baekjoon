a = int(input())
re=[]
for i in range(a):
  b = input()
  re.append(b)

re= list(set(re))
re =sorted(re)
re = sorted(re, key=len)
for i in re:
  print(i)