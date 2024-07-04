a = int(input())
sum = []
for i in range(a):
  a, b = map(int, input().split())
  sum.append(f"Case #{i+1}: {a} + {b} = {a+b}")

for i in sum:
  print(i)