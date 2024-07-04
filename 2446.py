a = int(input())
for i in range(a):
  print(" " * i + "*" * (2*a - 2*i-1))
for i in range(a - 2, -1, -1):
  print(" " * i + "*" * (2*a - 2*i-1))