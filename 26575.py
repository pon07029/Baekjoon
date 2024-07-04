a = int(input())
re=[]
for i in range(a):
  b,c,d= map(float, input().split())
  re.append(f"${round(b*c*d, 2):.2f}")

for i in re:
  print(i)