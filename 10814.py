import sys
n = int(sys.stdin.readline())
data = [sys.stdin.readline().split() for i in range(n)]

data.sort(key=lambda x : int(x[0]))

for i in data:
  print(i[0], i[1])