a = int(input())
sum = []
for i in range(a):
  a, b = map(int, input().split())
  sum.append(a+b)

for i in range(len(sum)):
  print(f"Case #{i+1}: {sum[i]}")