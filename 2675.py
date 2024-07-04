a = int(input())
re=[]
for i in range(a):
  c, b= map(str, input().split())
  re.append(''.join([i * int(c) for i in b]))

for i in re:
  print(i)