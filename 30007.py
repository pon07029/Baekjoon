d = int(input())
re=[]
for i in range(d):
  a, b, c= map(int, input().split())
  re.append(a*c+b-a)

for i in re:
  print(i)