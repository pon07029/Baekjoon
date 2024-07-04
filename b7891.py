a = int(input())
sum=[]
for i in range(a):
    x, y = map(int, input().split())

    sum.append(x+y)

for i in sum:
  print(i)