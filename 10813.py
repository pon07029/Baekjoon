import sys
a, b= map(int, input().split())

li = [i+1 for i in range(a)]
for i in range(b):
  a, b = map(int, sys.stdin.readline().split())
  li[a-1], li[b-1] = li[b-1], li[a-1]

print(*li)
