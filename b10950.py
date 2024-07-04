a = int(input())
sum = []
for i in range(a):
  a, b = map(int, input().split())
  sum.append(a+b)

for i in sum:
  print(i)