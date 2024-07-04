import sys
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

data.sort(key=lambda x : (x[0], x[1]))

for i in data:
  print(i[0], i[1])