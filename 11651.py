n = int(input())
re=[]
for i in range(n):
  a, b= map(int, input().split())
  re.append([a, b])

re.sort(key=lambda x: (x[1], x[0]))

for i in re:
  print(i[0], i[1])