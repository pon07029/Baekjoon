import sys

c, d = map(int, sys.stdin.readline().split())

lie = [i+1 for i in range(c)]

def reverse(li, a, b):
  le = li[a-1:b]
  le.reverse()
  li = li[:a-1] + le + li[b:]
  return  li


for i in range(d):
  a, b = map(int, sys.stdin.readline().split())
  lie = reverse(lie ,a, b)

print(*lie)

