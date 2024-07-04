import sys
import math
n = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(n)]

data.sort()
for i in data:
  print(i)
